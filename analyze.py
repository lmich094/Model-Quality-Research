"""
Regenerative Agriculture AI Study — Statistical Analysis
Factorial design: 5 framings × 3 lengths × 7 questions, two models (Claude, Codex)
Metrics: TD (1-5), CC (0+), RS (1-3), APK (1-3)
"""

import csv
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
        return "  —  "
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

print("=" * 70)
print("REGENERATIVE AGRICULTURE AI STUDY — ANALYSIS RESULTS")
print(f"Claude rows (excl. 1 ERROR): {len(claude_data)}")
print(f"Codex rows:                  {len(codex_data)}")
print(f"Total analysed:              {len(all_data)}")
print()
print("NOTE: Q7-PRO-S (Claude) was an ERROR response (no content generated).")
print("      It is excluded from all means; flagged in section 6.")
print("=" * 70)


# ── 1. Overall means by framing ───────────────────────────────────────────────

print("\n── 1. OVERALL MEANS BY FRAMING (pooled, both models, all questions) ──")
print(f"{'Framing':<8}", end="")
for m in METRICS:
    label = m if m != "word_count" else "words"
    print(f"  {label:>10}", end="")
print()
print("-" * 68)

for framing in FRAMING_ORDER:
    subset = [r for r in all_data if r["framing"] == framing]
    print(f"{framing:<8}", end="")
    for m in METRICS:
        vals = [r[m] for r in subset]
        print(f"  {fmt(mean(vals)):>10}", end="")
    print(f"  (n={len(subset)})")


# ── 2. Overall means by length ────────────────────────────────────────────────

print("\n── 2. OVERALL MEANS BY LENGTH (pooled, both models, all framings) ──")
print(f"{'Length':<8}", end="")
for m in METRICS:
    label = m if m != "word_count" else "words"
    print(f"  {label:>10}", end="")
print()
print("-" * 68)

for length in LENGTH_ORDER:
    subset = [r for r in all_data if r["length"] == length]
    print(f"{length:<8}", end="")
    for m in METRICS:
        vals = [r[m] for r in subset]
        print(f"  {fmt(mean(vals)):>10}", end="")
    print(f"  (n={len(subset)})")


# ── 3. Framing × length interaction: TD and RS ───────────────────────────────

print("\n── 3. FRAMING × LENGTH INTERACTION — mean TD / RS (pooled models) ──")
print(f"{'':8}  {'S':^13}  {'M':^13}  {'L':^13}")
print(f"{'Framing':<8}  {'TD':>5}  {'RS':>5}    {'TD':>5}  {'RS':>5}    {'TD':>5}  {'RS':>5}")
print("-" * 55)

for framing in FRAMING_ORDER:
    print(f"{framing:<8}", end="")
    for length in LENGTH_ORDER:
        subset = [r for r in all_data if r["framing"] == framing and r["length"] == length]
        td = mean([r["TD"] for r in subset])
        rs = mean([r["RS"] for r in subset])
        print(f"  {fmt(td):>5}  {fmt(rs):>5}", end="")
        if length != "L":
            print("  ", end="")
    print()


# ── 4. Model comparison ───────────────────────────────────────────────────────

print("\n── 4. MODEL COMPARISON — mean per metric ──")
print(f"{'Metric':<12}  {'Claude':>8}  {'Codex':>8}  {'Diff (Cl-Co)':>13}")
print("-" * 48)

for m in METRICS:
    label = m if m != "word_count" else "words"
    cm = mean([r[m] for r in claude_data])
    xm = mean([r[m] for r in codex_data])
    diff = cm - xm if (cm == cm and xm == xm) else float("nan")
    print(f"{label:<12}  {fmt(cm):>8}  {fmt(xm):>8}  {fmt(diff):>13}")

print(f"\n  Claude n={len(claude_data)} (104 valid responses, 1 ERROR excluded)")
print(f"  Codex  n={len(codex_data)} (105 responses)")


# ── 5. Domain-level TD spread ─────────────────────────────────────────────────

print("\n── 5. DOMAIN-LEVEL TD SPREAD (range of mean TD across 5 framings) ──")
print(f"{'Q':<5}  {'Domain':<22}  {'min TD':>6}  {'max TD':>6}  {'range':>6}")
print("-" * 50)

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
    print(f"{qid:<5}  {domain:<22}  {fmt(lo):>6}  {fmt(hi):>6}  {fmt(spread):>6}")


# ── 6. CC anomalies (CC ≥ 3) ─────────────────────────────────────────────────

print("\n── 6. CC ANOMALIES (CC ≥ 3) — partial/full refusals ──")
print(f"{'Model':<8}  {'prompt_id':<12}  {'framing':<8}  {'len':<4}  {'CC':>3}  Notes")
print("-" * 82)

anomalies = [r for r in all_data if r["CC"] is not None and r["CC"] >= 3]
if anomalies:
    for r in sorted(anomalies, key=lambda x: -x["CC"]):
        print(f"{r['model']:<8}  {r['pid']:<12}  {r['framing']:<8}  {r['length']:<4}  "
              f"{int(r['CC']):>3}  {r['notes']}")
else:
    print("  None found.")

print()
print("  FLAGGED ERROR (excluded from all analysis):")
print("  Claude     Q7-PRO-S     PRO      S     —  ERROR response — no content.")


# ── Interpretive Summary ───────────────────────────────────────────────────────

print("""
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
most sensitive to framing (highest TD spread) is the one where models
most strongly adjust technical depth in response to stated expertise,
confirming that both models do register and respond to framing signals
— the effect is just domain-contingent rather than universal.
""")
