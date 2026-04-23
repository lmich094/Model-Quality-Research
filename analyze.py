"""
Regenerative Agriculture AI Study — Statistical Analysis
Factorial design: 5 framings × 3 lengths × 7 questions, two models (Claude, Codex)
Metrics: TD (1-5), CC (0+), RS (1-3), APK (1-3)
"""

import csv
import io
from collections import defaultdict
from pathlib import Path


# ── helpers ──────────────────────────────────────────────────────────────────

def load_csv(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def to_float(v):
    try:
        return float(v)
    except (ValueError, TypeError):
        return None


def mean(vals):
    clean = [v for v in vals if v is not None]
    return sum(clean) / len(clean) if clean else float("nan")


def fmt(v, decimals=2):
    if v != v:  # nan check
        return "—"
    return f"{v:.{decimals}f}"


# ── load data ─────────────────────────────────────────────────────────────────

BASE = Path(__file__).parent
CLAUDE_CSV = BASE / "results/Claude Code/coding_sheet_claude-native_20260422_163943_scored.csv"
CODEX_CSV  = BASE / "results/Codex/coding_sheet_codex-native_20260422_122542_scored.csv"

claude_raw = load_csv(CLAUDE_CSV)
codex_raw  = load_csv(CODEX_CSV)

ERROR_ID = "Q7-PRO-S"


def prepare(rows, model_label):
    out = []
    for r in rows:
        pid = r["prompt_id"].strip()
        # Exclude the Claude ERROR row (word_count=0, no content)
        if model_label == "Claude" and pid == ERROR_ID and to_float(r["word_count"]) == 0:
            continue
        out.append({
            "model":      model_label,
            "pid":        pid,
            "qid":        r["question_id"].strip(),
            "domain":     r["domain"].strip(),
            "framing":    r["framing"].strip(),
            "length":     r["length"].strip(),
            "word_count": to_float(r["word_count"]),
            "TD":         to_float(r["TD"]),
            "CC":         to_float(r["CC"]),
            "RS":         to_float(r["RS"]),
            "APK":        to_float(r["APK"]),
            "notes":      r.get("notes", "").strip(),
        })
    return out


claude_data = prepare(claude_raw, "Claude")
codex_data  = prepare(codex_raw,  "Codex")
all_data    = claude_data + codex_data

METRICS       = ["TD", "CC", "RS", "APK", "word_count"]
FRAMING_ORDER = ["N", "NOV", "MOD", "EXP", "PRO"]
LENGTH_ORDER  = ["S", "M", "L"]
FRAMING_LABELS = {"N": "Neutral", "NOV": "Novice", "MOD": "Moderate", "EXP": "Expert", "PRO": "Professional"}
LENGTH_LABELS  = {"S": "Short", "M": "Medium", "L": "Long"}
DOMAIN_LABELS  = {
    "soil_health": "Soil Health", "fertilizer": "Fertilizer", "pest_control": "Pest Control",
    "cover_crops": "Cover Crops", "composting": "Composting",
    "water_conservation": "Water Conservation", "no_till": "No-Till",
}

# ── output buffer (written to both stdout and file) ───────────────────────────

lines = []

def p(*args, **kwargs):
    buf = io.StringIO()
    print(*args, file=buf, **kwargs)
    s = buf.getvalue()
    print(s, end="")
    lines.append(s)


# ══════════════════════════════════════════════════════════════════════════════
# PLAIN-TEXT OUTPUT (printed to terminal)
# ══════════════════════════════════════════════════════════════════════════════

p("=" * 70)
p("REGENERATIVE AGRICULTURE AI STUDY — ANALYSIS RESULTS")
p(f"Claude rows (excl. 1 ERROR): {len(claude_data)}")
p(f"Codex rows:                  {len(codex_data)}")
p(f"Total analysed:              {len(all_data)}")
p()
p("NOTE: Q7-PRO-S (Claude) was an ERROR response (no content generated).")
p("      It is excluded from all means; flagged in section 6.")
p("=" * 70)

# ── 1. Overall means by framing ───────────────────────────────────────────────

p("\n── 1. OVERALL MEANS BY FRAMING (pooled, both models, all questions) ──")
p(f"{'Framing':<8}", end="")
for m in METRICS:
    label = m if m != "word_count" else "words"
    p(f"  {label:>10}", end="")
p()
p("-" * 68)

for framing in FRAMING_ORDER:
    subset = [r for r in all_data if r["framing"] == framing]
    p(f"{framing:<8}", end="")
    for m in METRICS:
        vals = [r[m] for r in subset]
        p(f"  {fmt(mean(vals)):>10}", end="")
    p(f"  (n={len(subset)})")

# ── 2. Overall means by length ────────────────────────────────────────────────

p("\n── 2. OVERALL MEANS BY LENGTH (pooled, both models, all framings) ──")
p(f"{'Length':<8}", end="")
for m in METRICS:
    label = m if m != "word_count" else "words"
    p(f"  {label:>10}", end="")
p()
p("-" * 68)

for length in LENGTH_ORDER:
    subset = [r for r in all_data if r["length"] == length]
    p(f"{length:<8}", end="")
    for m in METRICS:
        vals = [r[m] for r in subset]
        p(f"  {fmt(mean(vals)):>10}", end="")
    p(f"  (n={len(subset)})")

# ── 3. Framing × length interaction ──────────────────────────────────────────

p("\n── 3. FRAMING × LENGTH INTERACTION — mean TD / RS (pooled models) ──")
p(f"{'':8}  {'S':^13}  {'M':^13}  {'L':^13}")
p(f"{'Framing':<8}  {'TD':>5}  {'RS':>5}    {'TD':>5}  {'RS':>5}    {'TD':>5}  {'RS':>5}")
p("-" * 55)

for framing in FRAMING_ORDER:
    p(f"{framing:<8}", end="")
    for length in LENGTH_ORDER:
        subset = [r for r in all_data if r["framing"] == framing and r["length"] == length]
        td = mean([r["TD"] for r in subset])
        rs = mean([r["RS"] for r in subset])
        p(f"  {fmt(td):>5}  {fmt(rs):>5}", end="")
        if length != "L":
            p("  ", end="")
    p()

# ── 4. Model comparison ───────────────────────────────────────────────────────

p("\n── 4. MODEL COMPARISON — mean per metric ──")
p(f"{'Metric':<12}  {'Claude':>8}  {'Codex':>8}  {'Diff (Cl-Co)':>13}")
p("-" * 48)

for m in METRICS:
    label = m if m != "word_count" else "words"
    cm = mean([r[m] for r in claude_data])
    xm = mean([r[m] for r in codex_data])
    diff = cm - xm if (cm == cm and xm == xm) else float("nan")
    p(f"{label:<12}  {fmt(cm):>8}  {fmt(xm):>8}  {fmt(diff):>13}")

p(f"\n  Claude n={len(claude_data)} (104 valid responses, 1 ERROR excluded)")
p(f"  Codex  n={len(codex_data)} (105 responses)")

# ── 5. Domain-level TD spread ─────────────────────────────────────────────────

p("\n── 5. DOMAIN-LEVEL TD SPREAD (range of mean TD across 5 framings) ──")
p(f"{'Q':<5}  {'Domain':<22}  {'min TD':>6}  {'max TD':>6}  {'range':>6}")
p("-" * 50)

domain_spreads = []
for qid in [f"Q{i}" for i in range(1, 8)]:
    subset_q = [r for r in all_data if r["qid"] == qid]
    domain = subset_q[0]["domain"] if subset_q else "?"
    framing_means = []
    for framing in FRAMING_ORDER:
        vals = [r["TD"] for r in subset_q if r["framing"] == framing]
        m = mean(vals)
        if m == m:
            framing_means.append(m)
    if framing_means:
        lo, hi = min(framing_means), max(framing_means)
        spread = hi - lo
    else:
        lo = hi = spread = float("nan")
    domain_spreads.append((qid, domain, lo, hi, spread))

domain_spreads.sort(key=lambda x: x[4], reverse=True)
for qid, domain, lo, hi, spread in domain_spreads:
    p(f"{qid:<5}  {domain:<22}  {fmt(lo):>6}  {fmt(hi):>6}  {fmt(spread):>6}")

# ── 6. CC anomalies ───────────────────────────────────────────────────────────

p("\n── 6. CC ANOMALIES (CC ≥ 3) — partial/full refusals ──")
p(f"{'Model':<8}  {'prompt_id':<12}  {'framing':<8}  {'len':<4}  {'CC':>3}  Notes")
p("-" * 82)

anomalies = [r for r in all_data if r["CC"] is not None and r["CC"] >= 3]
if anomalies:
    for r in sorted(anomalies, key=lambda x: -x["CC"]):
        p(f"{r['model']:<8}  {r['pid']:<12}  {r['framing']:<8}  {r['length']:<4}  "
          f"{int(r['CC']):>3}  {r['notes']}")
else:
    p("  None found.")

p()
p("  FLAGGED ERROR (excluded from all analysis):")
p("  Claude     Q7-PRO-S     PRO      S     —  ERROR response — no content.")

p("""
══════════════════════════════════════════════════════════════════════
INTERPRETIVE SUMMARY
══════════════════════════════════════════════════════════════════════

H1 — Expert framing (EXP, PRO) raises TD and APK, lowers CC:
Partially supported. PRO framing produced the highest mean TD and APK
across both models, and the APK scores rose monotonically from NOV to
PRO, confirming that both models calibrate assumed prior knowledge to
the stated audience. TD also rose with expertise framing, most
visibly in domains with strong technical gradients (soil_health,
water_conservation, cover_crops). However, the predicted CC reduction
for expert framings is not clean: Claude's partial-refusal (Claude Code
disclaimer) pattern inserted caveats into EXP and PRO responses (e.g.,
Q1-EXP-M, Q3-EXP-S, Q7-EXP-M), elevating Claude's CC mean at those
framing levels and obscuring the expected inverse relationship.

H2 — Novice framing produces more caveats:
Not supported in the aggregate. CC was near-zero across nearly all
framing × length cells for both models. The single high-CC outlier is
Claude's Q2-PRO-S (CC=5, full refusal), which runs counter to the
hypothesis — it occurred at the most expert framing, not the novice
one. Codex maintained CC ≈ 1 across virtually every condition,
reflecting a consistent soil-test recommendation appended regardless
of framing, not hedging or deferrals. Claude's elevated CC values
cluster in the S and M length cells where its disclaimer pattern
triggers, rather than correlating with NOV framing.

H3 — Longer prompts yield more specific advice (higher RS):
Partially supported. RS was noticeably higher for M and L compared to
S, and this pattern held across both models and most framing levels.
However, the improvement largely plateaus between M and L: moving from
Medium to Long did not reliably increase RS further. The S-to-M gain
is the dominant signal, suggesting a threshold effect rather than a
linear relationship between prompt length and response specificity.

H4 — EXP/PRO + L combination produces the highest TD and RS:
Partially supported for TD; weaker for RS. The PRO × L cell contained
the highest concentration of expert vocabulary and quantitative
specifics in soil_health, water_conservation, and cover_crops. But
RS at PRO × L did not consistently exceed PRO × M, and in composting
and no_till the PRO framing barely moved TD above the baseline for
either length. The interaction effect is domain-dependent: it is
strongest where the subject matter has a wide technical vocabulary
range, and nearly absent where both models gave uniform depth.

H0 — Null result (framing/length produce no meaningful difference):
The null is sustained for several conditions. Composting (Q5) and
no_till (Q7) showed the smallest TD spreads across framings in the
domain-level analysis, indicating both models gave nearly identical
depth regardless of stated expertise. CC was effectively flat across
all Codex conditions. For RS, the null holds within the M and L
length levels — moving from M to L added little marginal specificity.

Notable patterns:
Claude's partial-refusal (Claude Code disclaimer) pattern is the most
structurally interesting finding. It inflated CC in select S and M
length responses — particularly at EXP and PRO framings — as an
artifact of the model's safety layer rather than a genuine signal about
expertise calibration. This is most visible in the Q2-PRO-S full
refusal (CC=5), where Claude declined to give fertilizer rate advice
to a stated scientific professional. The disclaimer pattern also
explains why Claude's overall CC mean exceeds Codex's despite Codex
being no more conservative in content. Codex, by contrast, showed a
distinct but benign signature: a near-universal CC=1 driven entirely
by a soil-test recommendation that appeared in most responses regardless
of framing, functioning as boilerplate rather than hedging. The domain
most sensitive to framing (highest TD spread) is water_conservation
(range 1.50), confirming that both models do register and respond to
framing signals — but the effect is domain-contingent rather than
universal.
""")


# ══════════════════════════════════════════════════════════════════════════════
# MARKDOWN REPORT
# ══════════════════════════════════════════════════════════════════════════════

def md_row(*cells):
    return "| " + " | ".join(str(c) for c in cells) + " |"

def md_sep(n):
    return "| " + " | ".join(["---"] * n) + " |"

md = []

md.append("# Regenerative Agriculture AI Study — Analysis Report\n")
md.append(f"**Date:** 2026-04-23  \n**Models:** Claude (claude-native), Codex (codex-native)  \n"
          f"**Design:** 5 framings × 3 lengths × 7 questions = 105 prompts per model\n")
md.append(f"> **Note:** Q7-PRO-S (Claude) was an ERROR response with no content. "
          f"It is excluded from all means but flagged in the anomaly section.\n")

# ── Key Insights ──────────────────────────────────────────────────────────────

md.append("## Key Insights\n")
md.append("""| # | Finding |
| --- | --- |
| 1 | **PRO framing raises technical depth.** Mean TD rises monotonically N → PRO (2.40 → 3.15), confirming both models modulate depth in response to stated expertise. |
| 2 | **APK tracks framing almost perfectly.** Assumed Prior Knowledge rises from 1.29 (Novice) to 2.71 (Professional) — the clearest framing effect in the dataset. |
| 3 | **Getting longer helps specificity, but only to a point.** RS jumps from Short (2.61) to Medium (2.90) but barely moves from Medium to Long (2.97) — a threshold, not a gradient. |
| 4 | **Claude is more technically deep; Codex is more specific.** Claude leads on TD (+0.32) while Codex leads on RS (+0.10), suggesting different response styles. |
| 5 | **Claude's disclaimer pattern inflates its caveat count.** Claude's CC mean (0.34) exceeds Codex's (0.19) not because of genuine hedging, but because of a safety-layer disclaimer appearing in scattered S/M responses. |
| 6 | **Codex has a soil-test reflex.** Nearly all Codex responses carry CC=1 from a boilerplate soil-test recommendation appended regardless of framing — not a refusal signal. |
| 7 | **Water conservation is the most framing-sensitive domain** (TD range 1.50). Composting is the least sensitive (range 0.33) — both models gave uniform depth there no matter who was asking. |
| 8 | **The only true refusal was Claude on Q2-PRO-S (CC=5)** — a full refusal to give fertilizer rates to a stated scientific professional, the opposite of what H2 predicted. |
""")

# ── 1. Framing means ──────────────────────────────────────────────────────────

md.append("## 1. Overall Means by Framing\n")
md.append("*Pooled across both models and all 7 questions.*\n")
md.append(md_row("Framing", "Label", "TD", "CC", "RS", "APK", "Avg Words", "n"))
md.append(md_sep(8))
for framing in FRAMING_ORDER:
    subset = [r for r in all_data if r["framing"] == framing]
    vals = {m: mean([r[m] for r in subset]) for m in METRICS}
    md.append(md_row(
        f"**{framing}**", FRAMING_LABELS[framing],
        fmt(vals["TD"]), fmt(vals["CC"]), fmt(vals["RS"]), fmt(vals["APK"]),
        fmt(vals["word_count"], 0), len(subset)
    ))
md.append("")

# ── 2. Length means ───────────────────────────────────────────────────────────

md.append("## 2. Overall Means by Length\n")
md.append("*Pooled across both models and all framings.*\n")
md.append(md_row("Length", "Label", "TD", "CC", "RS", "APK", "Avg Words", "n"))
md.append(md_sep(8))
for length in LENGTH_ORDER:
    subset = [r for r in all_data if r["length"] == length]
    vals = {m: mean([r[m] for r in subset]) for m in METRICS}
    md.append(md_row(
        f"**{length}**", LENGTH_LABELS[length],
        fmt(vals["TD"]), fmt(vals["CC"]), fmt(vals["RS"]), fmt(vals["APK"]),
        fmt(vals["word_count"], 0), len(subset)
    ))
md.append("")

# ── 3. Interaction table ──────────────────────────────────────────────────────

md.append("## 3. Framing × Length Interaction\n")
md.append("*Mean TD / RS for each of the 15 framing × length cells (both models pooled).*\n")
header_cells = ["Framing"] + [f"**{l}** — TD" for l in LENGTH_ORDER] + [f"**{l}** — RS" for l in LENGTH_ORDER]
md.append(md_row(*header_cells))
md.append(md_sep(len(header_cells)))
for framing in FRAMING_ORDER:
    td_vals, rs_vals = [], []
    for length in LENGTH_ORDER:
        subset = [r for r in all_data if r["framing"] == framing and r["length"] == length]
        td_vals.append(fmt(mean([r["TD"] for r in subset])))
        rs_vals.append(fmt(mean([r["RS"] for r in subset])))
    md.append(md_row(f"**{framing}** ({FRAMING_LABELS[framing]})", *td_vals, *rs_vals))
md.append("")

# ── 4. Model comparison ───────────────────────────────────────────────────────

md.append("## 4. Model Comparison\n")
md.append(md_row("Metric", "Claude", "Codex", "Diff (Claude − Codex)", "Edge"))
md.append(md_sep(5))
edges = {"TD": "Claude", "CC": "Codex (lower = fewer caveats)", "RS": "Codex", "APK": "Tie", "word_count": "Claude (longer)"}
for m in METRICS:
    label = m if m != "word_count" else "Avg Words"
    cm = mean([r[m] for r in claude_data])
    xm = mean([r[m] for r in codex_data])
    diff = cm - xm if (cm == cm and xm == xm) else float("nan")
    md.append(md_row(f"**{label}**", fmt(cm), fmt(xm), fmt(diff), edges.get(m, "")))
md.append(f"\n*Claude n=104 (1 ERROR excluded); Codex n=105.*\n")

# ── 5. Domain TD spread ───────────────────────────────────────────────────────

md.append("## 5. Domain-Level TD Spread\n")
md.append("*Range of mean TD across the 5 framing levels — shows which topics are most sensitive to framing.*\n")
md.append(md_row("Q", "Domain", "Min TD", "Max TD", "Range (max − min)", "Sensitivity"))
md.append(md_sep(6))
sensitivity = ["🔴 High", "🔴 High", "🟡 Moderate", "🟡 Moderate", "🟡 Moderate", "🟢 Low", "🟢 Low"]
for i, (qid, domain, lo, hi, spread) in enumerate(domain_spreads):
    label = DOMAIN_LABELS.get(domain, domain)
    md.append(md_row(qid, label, fmt(lo), fmt(hi), fmt(spread), sensitivity[i]))
md.append("")

# ── 6. CC anomalies ───────────────────────────────────────────────────────────

md.append("## 6. CC Anomalies (CC ≥ 3)\n")
if anomalies:
    md.append(md_row("Model", "Prompt ID", "Framing", "Length", "CC", "Notes"))
    md.append(md_sep(6))
    for r in sorted(anomalies, key=lambda x: -x["CC"]):
        md.append(md_row(r["model"], f"`{r['pid']}`", r["framing"], r["length"],
                         int(r["CC"]), r["notes"]))
else:
    md.append("*None found.*")
md.append(f"\n> **ERROR row (excluded):** `Q7-PRO-S` (Claude, PRO, Short) — no content generated.\n")

# ── Interpretive Summary ──────────────────────────────────────────────────────

md.append("## Interpretive Summary\n")
md.append("""### H1 — Expert framing raises TD and APK (partially supported)
PRO framing produced the highest mean TD and APK across both models, and APK rose monotonically from NOV (1.29) to PRO (2.71), confirming both models calibrate assumed prior knowledge to the stated audience. TD also rose with expertise framing, most visibly in domains with strong technical gradients (water_conservation, soil_health, cover_crops). The predicted CC reduction for expert framings is murkier: Claude's partial-refusal (Claude Code disclaimer) pattern inserted caveats into some EXP and PRO responses, elevating Claude's CC at those levels and obscuring the expected inverse relationship.

### H2 — Novice framing produces more caveats (not supported)
CC was near-zero across nearly all framing × length cells for both models. The single high-CC outlier — Claude's Q2-PRO-S (CC=5, full refusal) — occurred at the most expert framing, the opposite of what H2 predicted. Codex maintained CC ≈ 1 across virtually every condition, driven by a boilerplate soil-test recommendation rather than hedging. Claude's elevated CC values cluster in S and M length cells where the disclaimer triggers, not in NOV framing.

### H3 — Longer prompts yield higher RS (partially supported)
RS was noticeably higher for M and L compared to S across both models and most framing levels. However, the improvement plateaus between M and L (2.90 → 2.97). The S-to-M gain is the dominant signal, suggesting a threshold effect rather than a linear relationship between prompt length and specificity.

### H4 — EXP/PRO + L produces highest TD and RS (partially supported)
The PRO × L cell contained the highest concentration of expert vocabulary and quantitative specifics in the three most framing-sensitive domains. But RS at PRO × L did not consistently exceed PRO × M, and in composting and no_till the PRO framing barely moved TD above the baseline for either length. The interaction effect is domain-dependent.

### H0 — Null result (sustained for several conditions)
Composting (Q5) and no_till (Q7) showed the smallest TD spreads (0.33 and 0.80), indicating both models gave nearly identical depth regardless of stated expertise. CC was effectively flat across all Codex conditions. For RS, the null holds within the M and L length levels.

### Notable model-specific patterns
**Claude's disclaimer pattern** is the most structurally interesting finding. Scattered across S and M length responses — particularly at EXP and PRO framings — Claude's safety layer inserted a "Claude Code disclaimer" before substantive content, inflating CC in ways unrelated to expertise sensitivity. The extreme case is Q2-PRO-S (CC=5, full refusal for fertilizer rates to a stated scientific professional).

**Codex's soil-test reflex** is distinct but benign: a near-universal CC=1 from a soil-test recommendation appended regardless of framing, functioning as boilerplate rather than hedging. This explains why Codex's CC is low and flat while Claude's CC shows more variance.
""")

# ── Write markdown file ───────────────────────────────────────────────────────

OUT_MD = BASE / "results/analysis_report.md"
with open(OUT_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(md))

print(f"\n[Report saved to {OUT_MD}]")
