# Regenerative Agriculture AI Study — Analysis Report

**Date:** 2026-04-23  
**Models:** Claude (claude-native), Codex (codex-native)  
**Design:** 5 framings × 3 lengths × 7 questions = 105 prompts per model

> **Note:** Q7-PRO-S (Claude) was an ERROR response with no content. It is excluded from all means but flagged in the anomaly section.

## Key Insights

| # | Finding |
| --- | --- |
| 1 | **PRO framing raises technical depth.** Mean TD rises monotonically N → PRO (2.40 → 3.15), confirming both models modulate depth in response to stated expertise. |
| 2 | **APK tracks framing almost perfectly.** Assumed Prior Knowledge rises from 1.29 (Novice) to 2.71 (Professional) — the clearest framing effect in the dataset. |
| 3 | **Getting longer helps specificity, but only to a point.** RS jumps from Short (2.61) to Medium (2.90) but barely moves from Medium to Long (2.97) — a threshold, not a gradient. |
| 4 | **Claude is more technically deep; Codex is more specific.** Claude leads on TD (+0.32) while Codex leads on RS (+0.10), suggesting different response styles. |
| 5 | **Claude's disclaimer pattern inflates its caveat count.** Claude's CC mean (0.34) exceeds Codex's (0.19) not because of genuine hedging, but because of a safety-layer disclaimer appearing in scattered S/M responses. |
| 6 | **Codex has a soil-test reflex.** Nearly all Codex responses carry CC=1 from a boilerplate soil-test recommendation appended regardless of framing — not a refusal signal. |
| 7 | **Water conservation is the most framing-sensitive domain** (TD range 1.50). Composting is the least sensitive (range 0.33) — both models gave uniform depth there no matter who was asking. |
| 8 | **The only true refusal was Claude on Q2-PRO-S (CC=5)** — a full refusal to give fertilizer rates to a stated scientific professional, the opposite of what H2 predicted. |

## 1. Overall Means by Framing

*Pooled across both models and all 7 questions.*

| Framing | Label | TD | CC | RS | APK | Avg Words | n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **N** | Neutral | 2.40 | 0.29 | 2.83 | 1.90 | 354 | 42 |
| **NOV** | Novice | 2.26 | 0.14 | 2.83 | 1.29 | 392 | 42 |
| **MOD** | Moderate | 2.45 | 0.19 | 2.81 | 2.00 | 382 | 42 |
| **EXP** | Expert | 2.79 | 0.36 | 2.81 | 2.19 | 410 | 42 |
| **PRO** | Professional | 3.15 | 0.34 | 2.85 | 2.71 | 451 | 41 |

## 2. Overall Means by Length

*Pooled across both models and all framings.*

| Length | Label | TD | CC | RS | APK | Avg Words | n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **S** | Short | 2.51 | 0.30 | 2.61 | 1.99 | 281 | 69 |
| **M** | Medium | 2.61 | 0.31 | 2.90 | 2.00 | 355 | 70 |
| **L** | Long | 2.70 | 0.17 | 2.97 | 2.06 | 556 | 70 |

## 3. Framing × Length Interaction

*Mean TD / RS for each of the 15 framing × length cells (both models pooled).*

| Framing | **S** — TD | **M** — TD | **L** — TD | **S** — RS | **M** — RS | **L** — RS |
| --- | --- | --- | --- | --- | --- | --- |
| **N** (Neutral) | 2.21 | 2.43 | 2.57 | 2.64 | 3.00 | 2.86 |
| **NOV** (Novice) | 2.07 | 2.36 | 2.36 | 2.57 | 2.93 | 3.00 |
| **MOD** (Moderate) | 2.21 | 2.43 | 2.71 | 2.57 | 2.86 | 3.00 |
| **EXP** (Expert) | 2.86 | 2.71 | 2.79 | 2.64 | 2.79 | 3.00 |
| **PRO** (Professional) | 3.23 | 3.14 | 3.07 | 2.62 | 2.93 | 3.00 |

## 4. Model Comparison

| Metric | Claude | Codex | Diff (Claude − Codex) | Edge |
| --- | --- | --- | --- | --- |
| **TD** | 2.77 | 2.45 | 0.32 | Claude |
| **CC** | 0.34 | 0.19 | 0.15 | Codex (lower = fewer caveats) |
| **RS** | 2.78 | 2.88 | -0.10 | Codex |
| **APK** | 2.03 | 2.00 | 0.03 | Tie |
| **Avg Words** | 419.05 | 376.82 | 42.23 | Claude (longer) |

*Claude n=104 (1 ERROR excluded); Codex n=105.*

## 5. Domain-Level TD Spread

*Range of mean TD across the 5 framing levels — shows which topics are most sensitive to framing.*

| Q | Domain | Min TD | Max TD | Range (max − min) | Sensitivity |
| --- | --- | --- | --- | --- | --- |
| Q6 | Water Conservation | 2.00 | 3.50 | 1.50 | 🔴 High |
| Q1 | Soil Health | 2.50 | 3.67 | 1.17 | 🔴 High |
| Q4 | Cover Crops | 2.67 | 3.67 | 1.00 | 🟡 Moderate |
| Q3 | Pest Control | 2.33 | 3.17 | 0.83 | 🟡 Moderate |
| Q7 | No-Till | 2.00 | 2.80 | 0.80 | 🟡 Moderate |
| Q2 | Fertilizer | 2.33 | 3.00 | 0.67 | 🟢 Low |
| Q5 | Composting | 2.00 | 2.33 | 0.33 | 🟢 Low |

## 6. CC Anomalies (CC ≥ 3)

| Model | Prompt ID | Framing | Length | CC | Notes |
| --- | --- | --- | --- | --- | --- |
| Claude | `Q2-PRO-S` | PRO | S | 5 | FULL REFUSAL. CC: opening disclaimer +1, consulting extension +1, soil testing +1, agronomic literature +1, peers in field +1. RS=1 (no actionable recs). |

> **ERROR row (excluded):** `Q7-PRO-S` (Claude, PRO, Short) — no content generated.

## Interpretive Summary

### H1 — Expert framing raises TD and APK (partially supported)
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
