# Inter-Rater Scoring Comparison Report

**Study:** Regenerative Agriculture AI Framing Study  
**Rater 1:** Claude Code  
**Rater 2:** Codex  
**Responses scored:** Claude-native (104 rows) + Codex-native (104 rows) = 208 paired rows  
*(Q7-PRO-S excluded as ERROR from all analyses)*

---

## 1. Overall Inter-Rater Agreement (Combined, n = 208)

| Dimension   |   N |   Mean_r1 |   Mean_r2 |   Mean_absdiff |   Max_absdiff |   Exact_agree_% |   Within1_agree_% |   Kappa_linear |   Pearson_r |
|:------------|----:|----------:|----------:|---------------:|--------------:|----------------:|------------------:|---------------:|------------:|
| TD          | 208 |     2.601 |     3.620 |          1.029 |             2 |          19.712 |            77.404 |          0.109 |       0.564 |
| CC          | 208 |     0.264 |     0.274 |          0.173 |             2 |          83.654 |            99.038 |          0.622 |       0.739 |
| RS          | 208 |     2.827 |     2.846 |          0.125 |             1 |          87.500 |           100.000 |          0.548 |       0.575 |
| APK         | 208 |     2.010 |     2.510 |          0.529 |             2 |          49.519 |            97.596 |          0.291 |       0.535 |

> **Interpretation guide**  
> Kappa (linear-weighted): ≥ 0.80 = near-perfect, 0.61–0.80 = substantial, 0.41–0.60 = moderate, < 0.41 = fair/poor.  
> Pearson r is reported for CC as a continuous count variable.

### 1a. Agreement — Claude model responses only (n = 104)

| Dimension   |   N |   Mean_r1 |   Mean_r2 |   Mean_absdiff |   Max_absdiff |   Exact_agree_% |   Within1_agree_% |   Kappa_linear |   Pearson_r |
|:------------|----:|----------:|----------:|---------------:|--------------:|----------------:|------------------:|---------------:|------------:|
| TD          | 104 |     2.769 |     3.606 |          0.856 |             2 |          29.808 |            84.615 |          0.193 |       0.589 |
| CC          | 104 |     0.337 |     0.394 |          0.154 |             2 |          86.538 |            98.077 |          0.755 |       0.837 |
| RS          | 104 |     2.779 |     2.875 |          0.154 |             1 |          84.615 |           100.000 |          0.482 |       0.559 |
| APK         | 104 |     2.029 |     2.490 |          0.500 |             2 |          51.923 |            98.077 |          0.333 |       0.562 |

### 1b. Agreement — Codex model responses only (n = 104)

| Dimension   |   N |   Mean_r1 |   Mean_r2 |   Mean_absdiff |   Max_absdiff |   Exact_agree_% |   Within1_agree_% |   Kappa_linear |   Pearson_r |
|:------------|----:|----------:|----------:|---------------:|--------------:|----------------:|------------------:|---------------:|------------:|
| TD          | 104 |     2.433 |     3.635 |          1.202 |             2 |           9.615 |            70.192 |          0.045 |       0.592 |
| CC          | 104 |     0.192 |     0.154 |          0.192 |             1 |          80.769 |           100.000 |          0.338 |       0.374 |
| RS          | 104 |     2.875 |     2.817 |          0.096 |             1 |          90.385 |           100.000 |          0.633 |       0.649 |
| APK         | 104 |     1.990 |     2.529 |          0.558 |             2 |          47.115 |            97.115 |          0.250 |       0.509 |

---

## 2. Scoring Variance Between Raters by Dimension

| Dimension   |   Inter-rater Diff Variance |   Mean |diff| |
|:------------|----------------------------:|--------------:|
| TD          |                       0.444 |         1.029 |
| APK         |                       0.329 |         0.529 |
| CC          |                       0.193 |         0.173 |
| RS          |                       0.125 |         0.125 |

**Dimension with highest inter-rater variance:** **TD**

---

## 3. Systematic Rater Bias (mean difference = r1 − r2)

Positive mean diff → Claude Code (r1) scores higher; negative → Codex (r2) scores higher.

| Dataset          | Dimension   |   Mean_diff (r1−r2) | Direction       |   t_stat | p_value   | Significant   |
|:-----------------|:------------|--------------------:|:----------------|---------:|:----------|:--------------|
| Claude responses | TD          |              -0.837 | rater2 > rater1 |  -12.468 | p < 0.001 | Yes           |
| Claude responses | CC          |              -0.058 | rater2 > rater1 |   -1.347 | p = 0.18  | No            |
| Claude responses | RS          |              -0.096 | rater2 > rater1 |   -2.566 | p = 0.01  | Yes           |
| Claude responses | APK         |              -0.462 | rater2 > rater1 |   -8.211 | p < 0.001 | Yes           |
| Codex responses  | TD          |              -1.202 | rater2 > rater1 |  -20.518 | p < 0.001 | Yes           |
| Codex responses  | CC          |               0.038 | rater1 > rater2 |    0.894 | p = 0.37  | No            |
| Codex responses  | RS          |               0.058 | rater1 > rater2 |    1.922 | p = 0.06  | No            |
| Codex responses  | APK         |              -0.538 | rater2 > rater1 |   -9.579 | p < 0.001 | Yes           |
| Combined         | TD          |              -1.019 | rater2 > rater1 |  -22.059 | p < 0.001 | Yes           |
| Combined         | CC          |              -0.010 | rater2 > rater1 |   -0.316 | p = 0.75  | No            |
| Combined         | RS          |              -0.019 | rater2 > rater1 |   -0.784 | p = 0.43  | No            |
| Combined         | APK         |              -0.500 | rater2 > rater1 |  -12.581 | p < 0.001 | Yes           |

---

## 4. Mean Absolute Disagreement by Framing

| Framing   |   N |   TD_MAD |   CC_MAD |   RS_MAD |   APK_MAD |
|:----------|----:|---------:|---------:|---------:|----------:|
| EXP       |  42 |    1.119 |    0.190 |    0.119 |     0.667 |
| MOD       |  42 |    0.929 |    0.095 |    0.143 |     0.381 |
| N         |  42 |    0.905 |    0.214 |    0.143 |     0.476 |
| NOV       |  42 |    0.857 |    0.095 |    0.119 |     0.810 |
| PRO       |  40 |    1.350 |    0.275 |    0.100 |     0.300 |

---

## 5. Mean Absolute Disagreement by Domain

| Domain             |   N |   TD_MAD |   CC_MAD |   RS_MAD |   APK_MAD |
|:-------------------|----:|---------:|---------:|---------:|----------:|
| composting         |  30 |    0.933 |    0.000 |    0.167 |     0.300 |
| cover_crops        |  30 |    0.633 |    0.300 |    0.333 |     0.367 |
| fertilizer         |  30 |    1.333 |    0.300 |    0.033 |     0.633 |
| no_till            |  28 |    1.357 |    0.000 |    0.036 |     0.643 |
| pest_control       |  30 |    1.100 |    0.000 |    0.133 |     0.700 |
| soil_health        |  30 |    0.600 |    0.567 |    0.167 |     0.400 |
| water_conservation |  30 |    1.267 |    0.033 |    0.000 |     0.667 |

---

## 6. Prompts with Largest Total Disagreement (top 20)

*(total_absdiff = sum of |diff| across TD, CC, RS, APK)*

| prompt_id   | model   | domain             | framing   | length   |   total_absdiff |   TD_diff |   CC_diff |   RS_diff |   APK_diff |
|:------------|:--------|:-------------------|:----------|:---------|----------------:|----------:|----------:|----------:|-----------:|
| Q1-EXP-M    | claude  | soil_health        | EXP       | M        |               4 |        -1 |         1 |        -1 |         -1 |
| Q4-NOV-S    | claude  | cover_crops        | NOV       | S        |               4 |        -1 |        -1 |        -1 |         -1 |
| Q6-NOV-L    | claude  | water_conservation | NOV       | L        |               4 |        -2 |         0 |         0 |         -2 |
| Q7-NOV-L    | claude  | no_till            | NOV       | L        |               4 |        -2 |         0 |         0 |         -2 |
| Q1-PRO-L    | codex   | soil_health        | PRO       | L        |               4 |        -2 |         1 |         0 |         -1 |
| Q2-N-L      | codex   | fertilizer         | N         | L        |               4 |        -2 |        -1 |         0 |         -1 |
| Q2-NOV-L    | codex   | fertilizer         | NOV       | L        |               4 |        -2 |         0 |         0 |         -2 |
| Q2-MOD-L    | codex   | fertilizer         | MOD       | L        |               4 |        -2 |         1 |         0 |         -1 |
| Q6-NOV-L    | codex   | water_conservation | NOV       | L        |               4 |        -2 |         0 |         0 |         -2 |
| Q7-NOV-L    | codex   | no_till            | NOV       | L        |               4 |        -2 |         0 |         0 |         -2 |
| Q1-PRO-M    | claude  | soil_health        | PRO       | M        |               3 |        -1 |        -2 |         0 |          0 |
| Q2-N-L      | claude  | fertilizer         | N         | L        |               3 |        -2 |         0 |         0 |         -1 |
| Q2-NOV-S    | claude  | fertilizer         | NOV       | S        |               3 |        -1 |        -1 |         0 |         -1 |
| Q2-NOV-M    | claude  | fertilizer         | NOV       | M        |               3 |        -2 |         0 |         0 |         -1 |
| Q2-PRO-S    | claude  | fertilizer         | PRO       | S        |               3 |        -1 |         2 |         0 |          0 |
| Q3-N-L      | claude  | pest_control       | N         | L        |               3 |        -1 |         0 |        -1 |         -1 |
| Q3-PRO-M    | claude  | pest_control       | PRO       | M        |               3 |        -2 |         0 |         0 |         -1 |
| Q3-PRO-L    | claude  | pest_control       | PRO       | L        |               3 |        -2 |         0 |         0 |         -1 |
| Q4-EXP-S    | claude  | cover_crops        | EXP       | S        |               3 |        -1 |        -1 |         0 |         -1 |
| Q5-EXP-S    | claude  | composting         | EXP       | S        |               3 |        -2 |         0 |         0 |         -1 |

### Pattern in Large Disagreements (total_absdiff ≥ 3)

Number of prompts: **55** out of 208

**By framing:**

- EXP: 17
- PRO: 12
- NOV: 11
- N: 9
- MOD: 6

**By domain:**

- fertilizer: 14
- no_till: 11
- water_conservation: 8
- soil_health: 7
- composting: 6
- pest_control: 5
- cover_crops: 4

**By length:**

- L: 27
- M: 15
- S: 13

**By model responses scored:**

- codex: 32
- claude: 23

---

## 7. Per-Model Agreement Summary

| Model   |   N |   TD_MAD |   TD_kappa |   CC_MAD |   CC_kappa |   RS_MAD |   RS_kappa |   APK_MAD |   APK_kappa |
|:--------|----:|---------:|-----------:|---------:|-----------:|---------:|-----------:|----------:|------------:|
| claude  | 104 |    0.856 |      0.193 |    0.154 |      0.755 |    0.154 |      0.482 |     0.500 |       0.333 |
| codex   | 104 |    1.202 |      0.045 |    0.192 |      0.338 |    0.096 |      0.633 |     0.558 |       0.250 |

---

## 8. Rubric Ambiguity and Rater Interpretation


### 8.1 TD — Technical Depth (most contentious dimension)

TD is the worst-performing dimension by every metric: kappa = 0.109 (near-random), mean absolute disagreement = 1.029, and exact agreement = only 19.7%. The bias is large and highly significant: Codex (rater2) scored TD *higher* than Claude Code (rater1) by 0.84 points on Claude responses and 1.20 points on Codex responses (both p < 0.001). Codex appears to treat the presence of domain vocabulary and structured formatting as sufficient for TD = 4–5, while Claude Code weighed mechanistic depth and source integration. **Recommendation:** The rubric's TD = 4 (advanced) vs TD = 5 (expert/scientific) anchors need concrete examples; raters should be trained together on at least 10 calibration responses.

### 8.2 APK — Assumed Prior Knowledge (second-most contentious)

APK kappa = 0.291 (fair). Codex (rater2) rated APK higher than Claude Code (rater1) by 0.46 on Claude responses and 0.54 on Codex responses (both p < 0.001). This suggests rater 2 read more jargon-laden responses as assuming more prior knowledge, while rater 1 credited in-text definitions as lowering the assumed baseline. The discrepancy is largest on NOV-framed prompts (APK_MAD = 0.810), where the two raters disagree most about whether the AI actually simplified its language. **Recommendation:** Clarify whether a response that uses jargon *but defines it* should be coded APK = 1 (novice) or APK = 2 (moderate).

### 8.3 CC — Caveat Count (good agreement overall, with model-specific drift)

CC showed reasonable agreement (kappa = 0.622, exact agreement = 83.7%), but the direction of bias flips by model: Claude Code scored *more* caveats on Claude model responses (mean diff = -0.06) yet *fewer* on Codex responses (mean diff = +0.04). Neither bias is statistically significant, but the sign reversal suggests rater familiarity with a model's hedging style may subtly influence counting. **Recommendation:** Add 3–4 anchor examples for CC = 0 vs CC ≥ 1, and blind raters to model identity during scoring.

### 8.4 RS — Recommendation Specificity (strongest agreement)

RS kappa = 0.548 and within-1 agreement = 100%, making it the most reliably scored dimension. The 1–3 scale and relatively unambiguous anchors (general vs. specific vs. quantified) keep raters aligned. Remaining disagreements occur at the RS = 2/3 boundary when a response lists steps but omits quantities or named products. **Recommendation:** Specify that RS = 3 requires at least one *named* product, quantity, or measurable outcome.

### 8.5 Framing and domain patterns

PRO and EXP framing prompted the most TD disagreement (MAD = 1.350 and 1.119), consistent with raters diverging on what "expertise-signaling" vocabulary actually means for technical depth. NOV framing drove the most APK disagreement (MAD = 0.810), highlighting the APK rubric gap noted above. By domain, fertilizer and no_till had the worst TD MAD (1.333 and 1.357 respectively), likely because these domains attract more technical jargon that raters weight differently. CC disagreement was highest for soil_health (0.567) and cover_crops (0.300), where hedged conditional advice ("if your soil pH is below 6...") may or may not be counted as a caveat.

### 8.6 Summary of recommendations

| Issue | Affected dimension | Recommendation |
|---|---|---|
| TD 1–5 boundary undefined | TD | Add anchor examples for each level; calibrate raters jointly |
| APK jargon-with-definition case | APK | Clarify APK = 1 vs 2 when terms are defined in-text |
| CC threshold inconsistency | CC | Add anchor examples for CC = 0 vs CC ≥ 1 |
| Model identity bias (CC) | CC | Blind raters to model identity during scoring |
| RS midpoint (2 vs 3) | RS | Require named product/quantity for RS = 3 |
