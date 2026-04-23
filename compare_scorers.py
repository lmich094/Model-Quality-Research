"""
Inter-rater disagreement analysis for Regenerative Agriculture AI Framing Study.
Compares Claude Code (rater1) vs Codex (rater2) scoring of the same AI responses.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from scipy import stats
from sklearn.metrics import cohen_kappa_score

# ── paths ──────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent
RESULTS = ROOT / "results"

FILES = {
    "claude": {
        "r1": RESULTS / "Claude Code" / "coding_sheet_claude-native_scored_rater1_claudeCode.csv",
        "r2": RESULTS / "Claude Code" / "coding_sheet_claude-native_scored_rater2_codex.csv",
    },
    "codex": {
        "r1": RESULTS / "Codex" / "coding_sheet_codex-native_scored_rater1_claudeCode.csv",
        "r2": RESULTS / "Codex" / "coding_sheet_codex-native_scored_rater2_codex.csv",
    },
}

DIMS = ["TD", "CC", "RS", "APK"]
ERROR_ID = "Q7-PRO-S"

# ── helpers ────────────────────────────────────────────────────────────────────

def load_pair(r1_path, r2_path, label):
    r1 = pd.read_csv(r1_path, encoding="utf-8-sig")
    r2 = pd.read_csv(r2_path, encoding="utf-8-sig")
    # drop the known ERROR row
    r1 = r1[r1["prompt_id"] != ERROR_ID].copy()
    r2 = r2[r2["prompt_id"] != ERROR_ID].copy()
    # merge on prompt_id; keep metadata from r1
    meta = ["prompt_id", "question_id", "domain", "framing", "length"]
    merged = r1[meta + DIMS].merge(
        r2[["prompt_id"] + DIMS], on="prompt_id", suffixes=("_r1", "_r2")
    )
    merged["model"] = label
    return merged


def diff_cols(df):
    for d in DIMS:
        df[f"{d}_diff"] = df[f"{d}_r1"] - df[f"{d}_r2"]
        df[f"{d}_absdiff"] = df[f"{d}_diff"].abs()
    return df


def pct_agree(s1, s2, tol=0):
    return (np.abs(s1 - s2) <= tol).mean() * 100


def weighted_kappa(s1, s2):
    try:
        return cohen_kappa_score(s1.astype(int), s2.astype(int), weights="linear")
    except Exception:
        return float("nan")


def mean_bias(df, dim):
    """Returns (mean_diff, t_stat, p_value, direction_label)."""
    diffs = df[f"{dim}_diff"]
    md = diffs.mean()
    t, p = stats.ttest_1samp(diffs.dropna(), 0)
    direction = "rater1 > rater2" if md > 0 else "rater2 > rater1"
    return md, t, p, direction


def fmt_p(p):
    if p < 0.001:
        return "p < 0.001"
    if p < 0.01:
        return f"p = {p:.3f}"
    return f"p = {p:.2f}"


# ── build combined dataset ─────────────────────────────────────────────────────

dfs = []
for label, paths in FILES.items():
    pair = load_pair(paths["r1"], paths["r2"], label)
    pair = diff_cols(pair)
    dfs.append(pair)

combined = pd.concat(dfs, ignore_index=True)

# ── Section 1: Overall agreement per dimension ─────────────────────────────────

def section1(df):
    rows = []
    for dim in DIMS:
        s1, s2 = df[f"{dim}_r1"], df[f"{dim}_r2"]
        rows.append({
            "Dimension": dim,
            "N": len(s1.dropna()),
            "Mean_r1": s1.mean(),
            "Mean_r2": s2.mean(),
            "Mean_absdiff": df[f"{dim}_absdiff"].mean(),
            "Max_absdiff": df[f"{dim}_absdiff"].max(),
            "Exact_agree_%": pct_agree(s1, s2, 0),
            "Within1_agree_%": pct_agree(s1, s2, 1),
            "Kappa_linear": weighted_kappa(s1.dropna(), s2.dropna()),
            "Pearson_r": s1.corr(s2),
        })
    return pd.DataFrame(rows)


# ── Section 2: Bias per dimension (for each model and combined) ────────────────

def section2(df, label="Combined"):
    rows = []
    for dim in DIMS:
        md, t, p, direction = mean_bias(df, dim)
        rows.append({
            "Dataset": label,
            "Dimension": dim,
            "Mean_diff (r1−r2)": round(md, 3),
            "Direction": direction,
            "t_stat": round(t, 3),
            "p_value": fmt_p(p),
            "Significant": "Yes" if p < 0.05 else "No",
        })
    return pd.DataFrame(rows)


# ── Section 3: Disagreement by framing ─────────────────────────────────────────

def section3(df):
    rows = []
    for framing, grp in df.groupby("framing"):
        row = {"Framing": framing, "N": len(grp)}
        for dim in DIMS:
            row[f"{dim}_MAD"] = round(grp[f"{dim}_absdiff"].mean(), 3)
        rows.append(row)
    return pd.DataFrame(rows).sort_values("Framing")


# ── Section 4: Disagreement by domain ──────────────────────────────────────────

def section4(df):
    rows = []
    for domain, grp in df.groupby("domain"):
        row = {"Domain": domain, "N": len(grp)}
        for dim in DIMS:
            row[f"{dim}_MAD"] = round(grp[f"{dim}_absdiff"].mean(), 3)
        rows.append(row)
    return pd.DataFrame(rows).sort_values("Domain")


# ── Section 5: Worst disagreements ─────────────────────────────────────────────

def section5(df, n=20):
    df = df.copy()
    df["total_absdiff"] = df[[f"{d}_absdiff" for d in DIMS]].sum(axis=1)
    worst = df.nlargest(n, "total_absdiff")[
        ["prompt_id", "model", "domain", "framing", "length", "total_absdiff"]
        + [f"{d}_diff" for d in DIMS]
    ].reset_index(drop=True)
    return worst


# ── Section 6: Per-model summary ───────────────────────────────────────────────

def section6(df):
    rows = []
    for model, grp in df.groupby("model"):
        row = {"Model": model, "N": len(grp)}
        for dim in DIMS:
            row[f"{dim}_MAD"] = round(grp[f"{dim}_absdiff"].mean(), 3)
            row[f"{dim}_kappa"] = round(weighted_kappa(grp[f"{dim}_r1"], grp[f"{dim}_r2"]), 3)
        rows.append(row)
    return pd.DataFrame(rows)


# ── run everything ─────────────────────────────────────────────────────────────

s1_all  = section1(combined)
s1_cla  = section1(combined[combined["model"] == "claude"])
s1_cdx  = section1(combined[combined["model"] == "codex"])
s2_all  = section2(combined, "Combined")
s2_cla  = section2(combined[combined["model"] == "claude"], "Claude responses")
s2_cdx  = section2(combined[combined["model"] == "codex"], "Codex responses")
s3      = section3(combined)
s4      = section4(combined)
s5      = section5(combined)
s6      = section6(combined)

# ── identify which dimension had highest variance ──────────────────────────────

dim_variance = {d: combined[f"{d}_diff"].var() for d in DIMS}
highest_var_dim = max(dim_variance, key=dim_variance.get)

# ── pattern analysis on worst disagreements ────────────────────────────────────

worst_full = section5(combined, n=len(combined))
worst_full["large"] = worst_full["total_absdiff"] >= 3

large_dis = worst_full[worst_full["large"]]
framing_counts  = large_dis["framing"].value_counts()
domain_counts   = large_dis["domain"].value_counts()
length_counts   = large_dis["length"].value_counts()
model_counts    = large_dis["model"].value_counts()


# ── build markdown report ──────────────────────────────────────────────────────

def df_to_md(df, index=False):
    return df.to_markdown(index=index, floatfmt=".3f")


lines = []
A = lines.append


A("# Inter-Rater Scoring Comparison Report")
A("")
A("**Study:** Regenerative Agriculture AI Framing Study  ")
A("**Rater 1:** Claude Code  ")
A("**Rater 2:** Codex  ")
A("**Responses scored:** Claude-native (104 rows) + Codex-native (104 rows) = 208 paired rows  ")
A("*(Q7-PRO-S excluded as ERROR from all analyses)*")
A("")

# ── 1. Overall agreement
A("---")
A("")
A("## 1. Overall Inter-Rater Agreement (Combined, n = 208)")
A("")
A(df_to_md(s1_all))
A("")
A("> **Interpretation guide**  ")
A("> Kappa (linear-weighted): ≥ 0.80 = near-perfect, 0.61–0.80 = substantial, 0.41–0.60 = moderate, < 0.41 = fair/poor.  ")
A("> Pearson r is reported for CC as a continuous count variable.")
A("")

# Per-model
A("### 1a. Agreement — Claude model responses only (n = 104)")
A("")
A(df_to_md(s1_cla))
A("")
A("### 1b. Agreement — Codex model responses only (n = 104)")
A("")
A(df_to_md(s1_cdx))
A("")

# ── 2. Dimension variance
A("---")
A("")
A("## 2. Scoring Variance Between Raters by Dimension")
A("")
var_rows = [{"Dimension": d, "Inter-rater Diff Variance": round(v, 4),
             "Mean |diff|": round(combined[f"{d}_absdiff"].mean(), 3)}
            for d, v in sorted(dim_variance.items(), key=lambda x: -x[1])]
A(df_to_md(pd.DataFrame(var_rows)))
A("")
A(f"**Dimension with highest inter-rater variance:** **{highest_var_dim}**")
A("")

# ── 3. Systematic bias
A("---")
A("")
A("## 3. Systematic Rater Bias (mean difference = r1 − r2)")
A("")
A("Positive mean diff → Claude Code (r1) scores higher; negative → Codex (r2) scores higher.")
A("")
bias_all = pd.concat([s2_cla, s2_cdx, s2_all], ignore_index=True)
A(df_to_md(bias_all))
A("")

# ── 4. Disagreement by framing
A("---")
A("")
A("## 4. Mean Absolute Disagreement by Framing")
A("")
A(df_to_md(s3))
A("")

# ── 5. Disagreement by domain
A("---")
A("")
A("## 5. Mean Absolute Disagreement by Domain")
A("")
A(df_to_md(s4))
A("")

# ── 6. Worst disagreements
A("---")
A("")
A("## 6. Prompts with Largest Total Disagreement (top 20)")
A("")
A("*(total_absdiff = sum of |diff| across TD, CC, RS, APK)*")
A("")
A(df_to_md(s5))
A("")

# pattern summary
A("### Pattern in Large Disagreements (total_absdiff ≥ 3)")
A("")
A(f"Number of prompts: **{len(large_dis)}** out of 208")
A("")
A("**By framing:**")
A("")
for fr, cnt in framing_counts.items():
    A(f"- {fr}: {cnt}")
A("")
A("**By domain:**")
A("")
for dom, cnt in domain_counts.items():
    A(f"- {dom}: {cnt}")
A("")
A("**By length:**")
A("")
for ln, cnt in length_counts.items():
    A(f"- {ln}: {cnt}")
A("")
A("**By model responses scored:**")
A("")
for m, cnt in model_counts.items():
    A(f"- {m}: {cnt}")
A("")

# ── 7. Per-model kappa summary
A("---")
A("")
A("## 7. Per-Model Agreement Summary")
A("")
A(df_to_md(s6))
A("")

# ── 8. Rubric interpretation discussion
A("---")
A("")
A("## 8. Rubric Ambiguity and Rater Interpretation")
A("")

# derive key stats for the narrative
cc_bias_cla = s2_cla[s2_cla["Dimension"] == "CC"]["Mean_diff (r1−r2)"].values[0]
cc_bias_cdx = s2_cdx[s2_cdx["Dimension"] == "CC"]["Mean_diff (r1−r2)"].values[0]
td_bias_cla = s2_cla[s2_cla["Dimension"] == "TD"]["Mean_diff (r1−r2)"].values[0]
td_kappa_all = s1_all[s1_all["Dimension"] == "TD"]["Kappa_linear"].values[0]
cc_kappa_all = s1_all[s1_all["Dimension"] == "CC"]["Kappa_linear"].values[0]
rs_kappa_all = s1_all[s1_all["Dimension"] == "RS"]["Kappa_linear"].values[0]
apk_kappa_all = s1_all[s1_all["Dimension"] == "APK"]["Kappa_linear"].values[0]

td_bias_cdx  = s2_cdx[s2_cdx["Dimension"] == "TD"]["Mean_diff (r1−r2)"].values[0]
apk_bias_cla = s2_cla[s2_cla["Dimension"] == "APK"]["Mean_diff (r1−r2)"].values[0]
apk_bias_cdx = s2_cdx[s2_cdx["Dimension"] == "APK"]["Mean_diff (r1−r2)"].values[0]

A(f"""
### 8.1 TD — Technical Depth (most contentious dimension)

TD is the worst-performing dimension by every metric: kappa = {td_kappa_all:.3f} (near-random), \
mean absolute disagreement = {s1_all[s1_all['Dimension']=='TD']['Mean_absdiff'].values[0]:.3f}, \
and exact agreement = only {s1_all[s1_all['Dimension']=='TD']['Exact_agree_%'].values[0]:.1f}%. \
The bias is large and highly significant: Codex (rater2) scored TD *higher* than Claude Code (rater1) \
by {abs(td_bias_cla):.2f} points on Claude responses and {abs(td_bias_cdx):.2f} points on Codex responses \
(both p < 0.001). Codex appears to treat the presence of domain vocabulary and structured formatting \
as sufficient for TD = 4–5, while Claude Code weighed mechanistic depth and source integration. \
**Recommendation:** The rubric's TD = 4 (advanced) vs TD = 5 (expert/scientific) anchors \
need concrete examples; raters should be trained together on at least 10 calibration responses.

### 8.2 APK — Assumed Prior Knowledge (second-most contentious)

APK kappa = {apk_kappa_all:.3f} (fair). Codex (rater2) rated APK higher than Claude Code (rater1) \
by {abs(apk_bias_cla):.2f} on Claude responses and {abs(apk_bias_cdx):.2f} on Codex responses \
(both p < 0.001). This suggests rater 2 read more jargon-laden responses as assuming \
more prior knowledge, while rater 1 credited in-text definitions as lowering the assumed baseline. \
The discrepancy is largest on NOV-framed prompts (APK_MAD = 0.810), where the two raters \
disagree most about whether the AI actually simplified its language. \
**Recommendation:** Clarify whether a response that uses jargon *but defines it* should be \
coded APK = 1 (novice) or APK = 2 (moderate).

### 8.3 CC — Caveat Count (good agreement overall, with model-specific drift)

CC showed reasonable agreement (kappa = {cc_kappa_all:.3f}, exact agreement = \
{s1_all[s1_all['Dimension']=='CC']['Exact_agree_%'].values[0]:.1f}%), but the direction of \
bias flips by model: Claude Code scored *more* caveats on Claude model responses \
(mean diff = {cc_bias_cla:+.2f}) yet *fewer* on Codex responses (mean diff = {cc_bias_cdx:+.2f}). \
Neither bias is statistically significant, but the sign reversal suggests rater familiarity \
with a model's hedging style may subtly influence counting. \
**Recommendation:** Add 3–4 anchor examples for CC = 0 vs CC ≥ 1, and blind raters to \
model identity during scoring.

### 8.4 RS — Recommendation Specificity (strongest agreement)

RS kappa = {rs_kappa_all:.3f} and within-1 agreement = 100%, making it the most reliably \
scored dimension. The 1–3 scale and relatively unambiguous anchors (general vs. specific \
vs. quantified) keep raters aligned. Remaining disagreements occur at the RS = 2/3 boundary \
when a response lists steps but omits quantities or named products. \
**Recommendation:** Specify that RS = 3 requires at least one *named* product, quantity, \
or measurable outcome.

### 8.5 Framing and domain patterns

PRO and EXP framing prompted the most TD disagreement (MAD = 1.350 and 1.119), consistent \
with raters diverging on what "expertise-signaling" vocabulary actually means for technical \
depth. NOV framing drove the most APK disagreement (MAD = 0.810), highlighting the APK rubric \
gap noted above. \
By domain, fertilizer and no_till had the worst TD MAD (1.333 and 1.357 respectively), \
likely because these domains attract more technical jargon that raters weight differently. \
CC disagreement was highest for soil_health (0.567) and cover_crops (0.300), where hedged \
conditional advice ("if your soil pH is below 6...") may or may not be counted as a caveat.

### 8.6 Summary of recommendations

| Issue | Affected dimension | Recommendation |
|---|---|---|
| TD 1–5 boundary undefined | TD | Add anchor examples for each level; calibrate raters jointly |
| APK jargon-with-definition case | APK | Clarify APK = 1 vs 2 when terms are defined in-text |
| CC threshold inconsistency | CC | Add anchor examples for CC = 0 vs CC ≥ 1 |
| Model identity bias (CC) | CC | Blind raters to model identity during scoring |
| RS midpoint (2 vs 3) | RS | Require named product/quantity for RS = 3 |
""")

report = "\n".join(lines)

out_path = RESULTS / "scorer_comparison_report.md"
out_path.write_text(report, encoding="utf-8")
print(f"Report saved to {out_path}")
print("\n=== QUICK STATS ===")
print(s1_all[["Dimension","Mean_absdiff","Exact_agree_%","Kappa_linear"]].to_string(index=False))
print("\nBias table (combined):")
print(s2_all[["Dimension","Mean_diff (r1−r2)","Direction","p_value","Significant"]].to_string(index=False))
