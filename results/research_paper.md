# Does Expertise Framing Change AI Advice?
## A Controlled Study of Regenerative Agriculture Responses from Claude and Codex

**Author:** Liam Michka
**Date:** April 2026

---

## Abstract

This study examines whether telling an AI model your level of expertise — from "I'm a complete novice" to "I'm a professional agronomist" — meaningfully changes the advice it gives. Using a fully factorial 5×3×7 design (105 prompts per model), we ran identical core questions about regenerative agriculture through two AI systems — Claude Sonnet 4.6 and OpenAI Codex — at five expertise framing levels and three prompt lengths. Two AI raters (Claude Code and Codex) independently scored all 210 responses on four dimensions: Technical Depth (TD), Caveat Count (CC), Recommendation Specificity (RS), and Assumed Prior Knowledge (APK). Expert framing did increase TD and APK monotonically (novice TD = 2.26 vs. professional TD = 3.15; novice APK = 1.29 vs. professional APK = 2.71), but did not reduce caveats as predicted — and the only full refusal in the dataset occurred at *professional* framing, not novice. Prompt length improved recommendation specificity (short RS = 2.61 → long RS = 2.97) but plateaued quickly after a medium-length prompt. Claude produced more technically deep, more verbose responses; Codex was marginally more specific. Inter-rater reliability was strong for CC (κ = 0.622) and RS (κ = 0.548) but near-random for TD (κ = 0.109) — the dimension most central to the study's question. (κ is Cohen's Kappa; see Section 3.6 for a full explanation.) Bottom line: stating your expertise level to an AI does change what you get, particularly vocabulary level and assumed background, but not in the simple "more expert = better advice" pattern most users might expect.

---

## 1. Introduction

When you ask a human expert for advice — a doctor, a lawyer, a seasoned farmer — the framing matters. Tell the doctor you're a nurse and they skip the basics. Tell them you have no medical background and they explain things from scratch. Whether they hedge more or less in either case is more nuanced than it first appears.

AI language models face the same prompt and make similar calibration decisions. The question this study asks is simple: **does telling an AI your expertise level change what it says?** And if so, how — does it get more technical? More specific? Less cautious?

This matters practically. Anyone who uses AI assistants regularly has probably wondered whether expertise framing affects response quality. The conventional wisdom — often passed around online — is that you should present yourself as an expert to get better responses. But "better" is vague. More technical isn't always better. More specific isn't always safer. And some of what looks like framing adaptation might be safety-layer behavior rather than genuine expertise calibration.

We chose regenerative agriculture as the domain because it spans a clean spectrum from common knowledge (composting, watering basics) to specialized expertise (soil biology, cover crop timing, no-till mechanics) — a domain where the difference between a novice question and an expert question genuinely matters, and where framing effects are plausible but not guaranteed.

### Research Questions

1. Does expertise framing (novice → professional) produce measurably different responses on technical depth, caveat frequency, specificity, and assumed prior knowledge?
2. Does prompt length independently affect response quality, and does it interact with framing?
3. Do two different AI models (Claude and Codex) respond differently to the same framing manipulations?
4. When two AI systems score the same responses independently, how reliably do they agree?

---

## 2. Methods

### 2.1 Study Design

The study used a fully crossed **5 × 3 × 7 factorial design**: five expertise framing levels, three prompt lengths, and seven domain questions, yielding 105 unique prompts per model. Both models received all 105 prompts. Total responses: 210 (before exclusions).

**Framing levels** were operationalized as a prefix sentence attached to an otherwise-identical core question. The five levels:

| Code | Label | Prefix text |
|------|-------|-------------|
| N | Neutral | *(no prefix — control condition)* |
| NOV | Novice | "I'm completely new to gardening and have never grown anything before." |
| MOD | Moderate | "I've been gardening for a couple of years but I'm still learning." |
| EXP | Expert | "I've been farming regeneratively for 20 years and hold a permaculture design certificate." |
| PRO | Professional | "I'm a professional agronomist with a background in soil science." |

**Prompt length levels** added context around the core question:

| Code | Description | Approx. word count |
|------|-------------|-------------------|
| S | Framing prefix + core question only | 10–45 words |
| M | + 3–4 sentences of situational context | 75–130 words |
| L | + 7–9 sentences of rich context | 170–280 words |

**Domain questions (Q1–Q7):**

| ID | Domain | Core question |
|----|--------|---------------|
| Q1 | Soil health | "What's the best way to improve soil health in my backyard garden?" |
| Q2 | Fertilizer | "Should I use compost or synthetic fertilizer for my vegetable beds?" |
| Q3 | Pest control | "How do I deal with pests in my garden without using pesticides?" |
| Q4 | Cover crops | "What cover crops should I plant to improve my soil over winter?" |
| Q5 | Composting | "How do I set up a simple composting system at home?" |
| Q6 | Water conservation | "What's the best way to conserve water in a backyard garden?" |
| Q7 | No-till | "How do I start a no-till garden bed from scratch?" |

The framing prefix was the only thing that differed across conditions for a given domain and length level. The core question was always identical.

### 2.2 Models Tested

| Model | Runner | Version | Temperature |
|-------|--------|---------|-------------|
| Claude | Claude Code runner | Claude Sonnet 4.6 | 0.0 |
| Codex | Codex CLI runner | OpenAI Codex | 0.0 |

Each prompt was sent as a single, isolated API call with no shared message history between prompts. Temperature was set to 0.0 to maximize reproducibility. Both runs were completed on April 22, 2026.

### 2.3 Scoring Rubric

All responses were scored on four dimensions (see Appendix A for full rubric with calibration anchors):

**Technical Depth (TD) — 1–5 scale.** Measures vocabulary and conceptual complexity. TD = 1 uses no technical terms; TD = 3 uses domain terms without always defining them; TD = 5 assumes expert-level fluency with specific application rates, mechanisms, and cultivar names.

**Caveat Count (CC) — raw integer.** A count of sentences that hedge, warn, or deflect responsibility (e.g., "you may want to consult an extension agent," "results will vary by region"). Factual conditionals ("if your soil is clay, drainage will be slower") are explicitly excluded.

**Recommendation Specificity (RS) — 1–3 scale.** RS = 1 is vague direction; RS = 2 names a method without quantities or timing; RS = 3 includes specific quantities, timing, products, or mechanisms.

**Assumed Prior Knowledge (APK) — 1–3 scale.** APK = 1 explains everything from first principles; APK = 2 assumes basic gardening familiarity; APK = 3 assumes domain expertise and skips fundamentals. Note: TD measures what vocabulary is *used*; APK measures whether the reader is expected to already *know* it.

### 2.4 Rater Setup

Two AI systems scored all responses independently:

- **Rater 1:** Claude Code (claude-sonnet-4-6)
- **Rater 2:** Codex

Each rater received the response text and the rubric and produced scores with brief justification notes. Raters were not shown each other's scores. The primary analysis uses Rater 1 (Claude Code) scores throughout for consistency; Rater 2 scores are used in the inter-rater reliability section. N = 208 paired rows — meaning 208 individual AI responses, each scored independently by both raters. Rater scores appear as two columns on the same row, not as separate rows, so the IRA dataset is 208 rows, not 418. For reference: the raw response count is 104 Claude + 105 Codex = 209 responses; Q7-PRO-S is excluded from both rater sets, leaving 208.

### 2.5 Exclusions

**Q7-PRO-S (Claude model):** No content was generated (word count = 0). Excluded from all analysis. Effective N: 104 Claude rows, 105 Codex rows.

**Q2-PRO-S (Claude model):** Full refusal — scored as CC = 5, RS = 1. Retained in analysis as a valid data point, since the refusal itself is a meaningful observation.

---

## 3. Results

### 3.1 Effect of Expertise Framing

Throughout Sections 3.1, 3.2, and 3.4, **pooled models** means Claude and Codex responses are combined into a single dataset — 104 Claude rows and 105 Codex rows treated as one group — to isolate the effect of the variable being examined (framing or length) from model-level differences. Model-specific differences are reported separately in Section 3.3.

**Table 1. Mean scores by expertise framing (n ≈ 41–42 per framing, pooled models, Rater 1 scores)**

| Framing | TD | CC | RS | APK | Avg. words |
|---------|-----|-----|-----|-----|-----------|
| N (Neutral) | 2.40 | 0.29 | 2.83 | 1.90 | 354 |
| NOV (Novice) | 2.26 | 0.14 | 2.83 | 1.29 | 392 |
| MOD (Moderate) | 2.45 | 0.19 | 2.81 | 2.00 | 382 |
| EXP (Expert) | 2.79 | 0.36 | 2.81 | 2.19 | 410 |
| PRO (Professional) | 3.15 | 0.34 | 2.85 | 2.71 | 451 |

The clearest framing effect is on **APK**, which rises monotonically from 1.29 (novice) to 2.71 (professional) — a shift of 1.42 points on a 3-point scale. This suggests AI models genuinely calibrate assumed background knowledge to stated expertise. **TD** also increases steadily (2.26 → 3.15), though the absolute shift is smaller on its 5-point scale.

**RS shows almost no response to framing** — scores cluster between 2.81 and 2.85 regardless of who is asking. Specificity appears driven by other factors (see Section 3.2).

**CC is the most counterintuitive result.** The novice framing (NOV) has the *lowest* CC (0.14) of any condition. The highest values occur at EXP (0.36) and PRO (0.34). This directly contradicts the prediction that novice prompts attract more safety language — discussed further in Section 4.

Response length increases modestly with expertise framing (354 → 451 average words from N to PRO), suggesting models generate slightly more verbose responses to apparently expert audiences.

### 3.2 Effect of Prompt Length

**Table 2. Mean scores by prompt length (n ≈ 69–70 per level, pooled models, Rater 1 scores)**

| Length | TD | CC | RS | APK | Avg. words |
|--------|-----|-----|-----|-----|-----------|
| S (Short) | 2.51 | 0.30 | 2.61 | 1.99 | 281 |
| M (Medium) | 2.61 | 0.31 | 2.90 | 2.00 | 355 |
| L (Long) | 2.70 | 0.17 | 2.97 | 2.06 | 556 |

Length has its clearest effect on **RS**: the jump from short to medium prompts (2.61 → 2.90) is substantial, but the further step from medium to long adds only 0.07 points (2.97). This is a **threshold effect rather than a linear gradient** — providing a few sentences of context makes recommendations considerably more specific; providing considerably more context after that adds little.

**CC decreases from medium to long (0.31 → 0.17).** Longer, richer prompts attract *fewer* caveats. One interpretation: more context reduces the apparent ambiguity of the situation, giving the model less reason for defensive hedging.

**APK is nearly flat across length levels** (1.99 → 2.00 → 2.06), confirming that assumed prior knowledge is driven primarily by framing (who you say you are) rather than how much context you provide.

### 3.3 Model Comparison

**Table 3. Claude vs. Codex mean scores (Rater 1 scores, n ≈ 104 per model)**

| Metric | Claude | Codex | Difference |
|--------|--------|-------|-----------|
| TD | 2.77 | 2.45 | +0.32 (Claude higher) |
| CC | 0.34 | 0.19 | +0.15 (Claude higher) |
| RS | 2.78 | 2.88 | +0.10 (Codex higher) |
| APK | 2.03 | 2.00 | ~tie |
| Words | 419 | 377 | +42 (Claude longer) |

Claude responses score higher on technical depth and produce more caveats; Codex responses are slightly more specific in their recommendations. The 42-word average difference in response length is a stylistic distinction — Claude elaborates more — rather than a direct quality difference.

APK is nearly identical across models. Both systems appear to calibrate assumed-reader level similarly when receiving the same framing, even though they differ in how technically deep or specific their responses are.

### 3.4 Domain Sensitivity to Framing

Not all topics responded equally to expertise framing. Table 4 shows the range of TD scores across the five framing levels for each domain (pooled models, Rater 1).

**Table 4. TD sensitivity to framing by domain (range = max − min across framing levels)**

| Domain | TD range | Sensitivity |
|--------|----------|------------|
| Water conservation | 1.50 | High |
| Soil health | 1.17 | High |
| Cover crops | 1.00 | Moderate |
| Pest control | 0.83 | Moderate |
| No-till | 0.80 | Moderate |
| Fertilizer | 0.67 | Low |
| Composting | 0.33 | Very low |

Water conservation and soil health show the largest framing-driven TD variation — these topics have a wider depth spectrum that models exploit when signaled about expertise. Composting shows minimal TD change regardless of who is asking, which is arguably the most intuitive null result: at the backyard scale, a composting system is a composting system. There is a ceiling on relevant technical depth that the models seem to reach early regardless of framing.

### 3.5 Notable Anomalies

**The Claude disclaimer pattern.** Nine Claude responses — spanning neutral, moderate, and expert framings at short and medium lengths — contained a boilerplate Claude Code interface disclaimer that mechanically added +1 to their CC score. This is a runner-environment artifact, not a genuine content signal. After adjusting for it, the Claude–Codex CC gap shrinks from 0.15 to approximately 0.06 overall, and the MOD framing gap closes to zero entirely. Without identifying this artifact, Claude would appear systematically more cautious than it actually is.

**Q2-PRO-S: A full refusal at professional framing.** For the fertilizer question at professional framing and short prompt length, Claude refused to provide application rates, generating CC = 5 and RS = 1 — the only true content refusal in the dataset. The refusal text cited uncertainty about local conditions and recommended consulting agronomic literature and professional peers. This is the opposite of H2's prediction: the model declined to give specific advice to a stated *professional*, not a novice. It appears to represent a liability-avoidance trigger specific to actionable chemical guidance, not a general response to expertise framing.

**The Codex soil-test reflex.** Codex appended a boilerplate soil-test recommendation to nearly every response across all framing levels, producing CC ≈ 1 in most Codex rows regardless of the question or the stated expertise of the asker. This is house style — a systematic low-intensity suggestion — rather than framing-responsive hedging. It means Codex's low overall CC (0.19) reflects consistent background-level caution, not an absence of cautionary language.

### 3.6 Inter-Rater Reliability

**Cohen's Kappa (κ)** is a standard measure of agreement between two raters that corrects for chance. If two raters would agree 60% of the time just by guessing randomly, a raw 70% agreement rate isn't impressive — κ accounts for that baseline and reports only the agreement above chance. κ = 1.0 means perfect agreement; κ = 0.0 means agreement is no better than chance; negative κ means raters disagree more than chance would predict. Conventional benchmarks: < 0.20 slight, 0.21–0.40 fair, 0.41–0.60 moderate, 0.61–0.80 substantial, > 0.80 near-perfect. Linear-weighted κ (used here) gives partial credit for near-misses, so a 1-point disagreement is penalized less than a 3-point disagreement.

**Table 5. Inter-rater reliability (Rater 1 = Claude Code, Rater 2 = Codex; n = 208 paired rows)**

| Dimension | Mean \|r1−r2\| | Exact agree % | Linear κ | Systematic bias |
|-----------|--------------|---------------|----------|----------------|
| TD | 1.03 | 19.7% | 0.109 | Codex +1 pt higher (p < 0.001) |
| APK | 0.53 | 49.5% | 0.291 | Codex +0.50 higher (p < 0.001) |
| RS | 0.13 | 87.5% | 0.548 | None significant |
| CC | 0.17 | 83.7% | 0.622 | None significant |

**CC and RS are reliably scored** (κ = 0.622 and 0.548 respectively). Both raters tend to agree on whether a response contained a hedge and how specific a recommendation was — these are relatively discrete, criterion-referenced judgments.

**TD is the most problematic dimension.** Raters agreed exactly on only 1 in 5 scores. Linear weighted kappa is 0.109, near-random agreement. More importantly, Codex as a rater systematically scores TD approximately 1 full point higher than Claude Code (p < 0.001). This reflects a genuine interpretive difference: Codex appears to treat the presence of domain vocabulary as sufficient for a high TD score, while Claude Code weights the sophistication of the underlying reasoning, not just the vocabulary used.

**APK shows fair reliability** (κ = 0.291). The largest disagreements cluster at novice framing (mean absolute disagreement = 0.810 at NOV), where raters frequently diverged on whether the AI actually simplified its language or merely maintained normal vocabulary while reducing assumed context.

A notable structural quirk: **CC bias flips sign by model**. Claude Code scores more caveats on Claude responses, and Codex scores more caveats on Codex responses. This hints at rater-familiarity effects — each rater may be better calibrated to recognize hedging patterns in the model it knows best.

The 55 prompts with total disagreement ≥ 3 points concentrate at PRO and EXP framings, fertilizer and no-till domains, and long prompts — exactly the conditions expected to produce the most expert-targeted responses, where rubric anchors are least clear.

---

## 4. Discussion

### 4.1 Hypothesis Verdicts

**H1 — Expert framing produces more technical, less caveated responses: Partially supported.**

The "more technical" part holds clearly. TD increases from 2.26 (NOV) to 3.15 (PRO), and APK shows an even cleaner gradient (1.29 → 2.71). The "fewer caveats" part failed: expert framings did not lower CC. If anything, EXP and PRO attracted marginally more caveats than NOV, driven partly by the Q2-PRO-S refusal and partly by Claude's disclaimer artifact. AI models do calibrate vocabulary and assumed background to stated expertise — they do not calibrate their caution level in the same direction.

**H2 — Novice framing produces more safety warnings: Not supported.**

NOV produced the lowest CC (0.14) of any framing. This is one of the clearest null results in the study. The highest-caveat event in the dataset happened at PRO framing. One interpretation: the models may treat stated expertise as a signal that the stakes are higher, not lower, and calibrate caution accordingly. Alternatively, the Q2-PRO-S refusal is idiosyncratic — fertilizer rates may carry specific liability triggers — and doesn't generalize. Either way, the simple "novice = more warnings" prediction is not what happened.

**H3 — Longer prompts produce more tailored advice: Partially supported.**

RS improves with length (2.61 → 2.90 → 2.97), but the gain is front-loaded. Going from a bare question to a medium-length prompt produces almost all the specificity benefit. Adding substantially more context after that contributes minimally. There's a threshold below which the AI gives generic advice and above which it gets specific — but more context beyond that threshold doesn't keep helping.

**H4 — Expert + long prompt produces the most actionable responses: Partially supported.**

PRO-L responses have the highest average TD. But RS reaches its ceiling (3.00) across essentially all long-prompt cells regardless of framing. A novice with a long prompt gets advice just as specific as a professional with a long prompt — they just get advice that assumes less background. *Tailored for expertise* and *more actionable* are not the same thing, and it's worth keeping that distinction clear.

**H0 — Framing produces no meaningful difference: Partially valid.**

For RS across all conditions and for CC under most conditions, framing produces negligible differences. For composting specifically, framing is essentially irrelevant. The meaningful framing effects are real, but they're concentrated in specific dimensions (TD, APK) and vary substantially by domain.

### 4.2 What the Framing Effects Actually Mean

The clearest story from this data: AI models calibrate **vocabulary level and assumed reader background** to stated expertise, but not the **content structure or safety level** of their advice.

A professional agronomist and a complete novice tend to get recommendations with similar specificity and similar rates of hedging. But the professional gets a response that assumes they know what mycorrhizal fungi are, what a C:N ratio is, and why soil biology matters — skipping definitions the novice would get.

Whether this represents genuine expertise calibration or surface-level statistical pattern matching on vocabulary associated with expertise in training data is an open question. The behavioral pattern is consistent and measurable. Its underlying mechanism is not resolvable from this data.

### 4.3 The Disclaimer Artifact and What It Reveals

The nine Claude responses containing the interface disclaimer illustrate a broader methodological point: **model safety layers and interface-specific behaviors can add systematic signal to scores that looks like framing-responsive behavior but isn't.** Without identifying the artifact, Claude would appear more cautious than Codex. After correction, the gap is minimal.

This has implications for any study of AI response behavior: the runner environment (which client or interface the model is accessed through) is a confound that needs to be controlled or at least identified. The same model accessed through Claude.ai, the API directly, and Claude Code may produce meaningfully different caveat profiles simply due to interface-level messaging that has nothing to do with the prompt content.

### 4.4 IRA Implications: Can AI Systems Score AI Responses?

The inter-rater results present a split verdict. For discrete, countable, or criterion-referenced dimensions — count the hedges, determine if a specific quantity was given — two AI raters agree reliably (κ = 0.548–0.622). For impression-based dimensions that require holistic judgment about sophistication and depth (TD, APK), they diverge substantially, with near-random agreement on the primary outcome dimension.

This matters because TD is central to the study's question. The finding that our two AI raters agree near-randomly on that dimension is a genuine limitation, and the systematic one-point bias between raters means that results depend meaningfully on *which* rater's scores you use.

The practical upshot for anyone considering AI-as-rater designs: AI systems can reliably handle discrete, countable judgments. For holistic quality assessments, the current evidence suggests human raters still add substantial value — particularly when the rubric requires fine-grained distinctions between adjacent levels.

---

## 5. Limitations

**Small N in some cells.** With 105 prompts per model and a 5×3×7 design, many cells contain a single response. The results are descriptive rather than inferential, and no statistical significance testing is reported beyond the IRA bias tests.

**Single domain.** All questions concern regenerative agriculture. Framing effects may differ substantially in medical, legal, or other technical domains where expertise signals carry different weights or activate different safety behaviors.

**AI raters, not human raters.** The IRA analysis shows that AI raters disagree substantially on holistic dimensions. The primary analysis uses Rater 1 scores, but those scores themselves carry uncertainty. Human rater validation would strengthen confidence in the absolute values.

**Rubric ambiguity on TD.** The TD = 3 / TD = 4 boundary (domain terms used vs. mechanisms assumed) is the primary driver of rater disagreement. A more operationalized rubric with explicit vocabulary checklists would likely reduce this.

**One snapshot of model versions.** Both models were tested in a single session in April 2026. Model behavior changes across versions; the patterns observed here are version-specific.

**Temperature 0.0 reduces but doesn't eliminate variance.** A single run per prompt doesn't quantify response variability. Some variability may remain even at T = 0.

**Q2-PRO-S may be idiosyncratic.** This single data point generates outsized interpretive weight in the CC and refusal analysis. Fertilizer rate advice may have specific liability triggers in Claude's training that don't generalize.

---

## 6. Implications for AI Users

### 6.1 General: Does Stating Your Expertise Level Actually Help?

Yes, but specifically. Telling an AI you're an expert will get you a response that skips definitional scaffolding, uses domain vocabulary without apology, and assumes you understand the underlying mechanisms. It will not reliably make recommendations more specific or more actionable — those dimensions are driven more by how much context you provide than by who you say you are.

The practical takeaway: **state your expertise level to get terminology-matched responses; add detailed situational context to get actionable recommendations.** These are partially independent levers. Combining them (expert framing + medium-to-long prompt) produces the highest TD and APK, but RS reaches its ceiling at medium prompt length regardless.

Across both models, moving from novice to professional framing increased TD by about 1 point on a 5-point scale and APK by 1.4 points on a 3-point scale — real differences, but not transformative ones. Most of the gain in RS came from adding context, not from claiming expertise.

### 6.2 Claude-Specific: When Does Safety-Layer Behavior Appear?

Claude's safety behavior appeared in two distinct forms. The interface disclaimer pattern (nine rows, +1 CC) is an artifact of the runner environment — it doesn't reflect prompt-level caution. The Q2-PRO-S full refusal is substantive: Claude declined to give fertilizer application rates to a stated scientific professional. The refusal cited local conditions and recommended consulting peer literature — consistent with a liability-avoidance heuristic rather than expertise calibration.

For Claude users: **if you're asking about topics with clear applied risk (fertilizer rates, pesticide dosages, chemical applications), expertise framing may not override the safety layer.** Reframing toward underlying mechanisms rather than actionable rates may be more productive. For the broad range of regenerative agriculture questions tested here, Claude was responsive to expertise framing in the TD and APK dimensions without significant safety friction.

### 6.3 Codex: The Boilerplate Reflex

Codex appended a boilerplate soil-test recommendation to nearly every response regardless of framing. This is a systematic pattern — a low-intensity hedge that functions as background noise rather than a genuine response to uncertainty. Codex's lower overall CC (0.19) relative to Claude's raw score (0.34) reflects this consistent low-level pattern rather than an absence of hedging language. After correcting for Claude's interface disclaimer artifact, the gap shrinks to approximately 0.06 — essentially equivalent.

Codex responses tended to be slightly more specific (RS = 2.88 vs. 2.78) and slightly less technically deep (TD = 2.45 vs. 2.77) than Claude. In practical terms: Codex gives you something concrete to do; Claude gives you more conceptual background. Which is more useful depends on what you need.

---

## 7. Future Directions

**Human rater replication.** Having working farmers or agronomists score a representative subset of responses with the same rubric would establish whether the AI raters' systematic biases reflect genuine interpretive differences or rubric failures.

**Other domains.** Medical, legal, and technical domains may show different framing sensitivities — particularly for CC, where expertise signals might more predictably trigger safety-layer responses.

**Longitudinal model version tracking.** Running the same 105 prompts against newer model versions over time would quantify how framing sensitivity changes with training updates.

**Refined rubric for TD and APK.** Future iterations should operationalize TD anchors with explicit vocabulary checklists (e.g., "TD = 4 responses use at least two of: mycorrhizal, C:N ratio, soil aggregate stability, phosphorus cycling...") to reduce rater disagreement.

**Testing downstream effects.** The most practically relevant follow-on question: does receiving a TD = 4 response versus a TD = 2 response actually change what a user does? If the advice is more technical but not more actionable, does the framing effect translate to real-world benefit?

---

## Appendix A: Scoring Rubric

**Technical Depth (TD) — 1–5**

| Score | Description |
|-------|-------------|
| 1 | No technical terms; explains from first principles ("Soil is where plants get their food.") |
| 2 | Basic terms used but defined inline ("Nitrogen — a key nutrient plants need — can be...") |
| 3 | Domain terms used without always defining ("Add blood meal or compost tea.") |
| 4 | Assumes familiarity with practices/mechanisms ("Inoculate legume seeds to maximize N fixation.") |
| 5 | Expert-level: application rates, mechanisms, cultivar names ("Apply 2 lbs/1000 sq ft feather meal; target C:N ratio 25:1.") |

*Calibration note: the TD = 3 / TD = 4 boundary is the critical distinction. TD = 3 is action-focused; TD = 4 assumes you already know why.*

**Caveat Count (CC) — raw integer**

Count sentences that hedge, warn, or deflect responsibility.

Examples that count: "You may want to consult an extension agent." / "Results will vary by region." / "Every garden is different."

Examples that do NOT count: "If your soil is clay, drainage will be slower." / "Sandy soils drain faster than clay."

**Recommendation Specificity (RS) — 1–3**

| Score | Description |
|-------|-------------|
| 1 | Vague direction ("Improve your soil with organic matter.") |
| 2 | Method named, no quantities/timing/products ("Add compost in fall.") |
| 3 | Specific quantities, timing, products, or mechanisms ("Apply 2–4 inches of compost before first frost; plant crimson clover at 15 lbs/acre.") |

**Assumed Prior Knowledge (APK) — 1–3**

| Score | Description |
|-------|-------------|
| 1 | Explains everything from first principles; zero prior knowledge assumed |
| 2 | Assumes basic gardening familiarity (knows what compost is) |
| 3 | Assumes domain expertise; skips fundamentals without explanation |

---

## Appendix B: Expertise Framing Prefixes

| Code | Full prefix text |
|------|-----------------|
| N | *(no prefix — control condition)* |
| NOV | "I'm completely new to gardening and have never grown anything before." |
| MOD | "I've been gardening for a couple of years but I'm still learning." |
| EXP | "I've been farming regeneratively for 20 years and hold a permaculture design certificate." |
| PRO | "I'm a professional agronomist with a background in soil science." |

All framing prefixes were prepended to the same core question for a given domain and length level. The core question was identical across all five framing conditions within each domain × length combination.

---

## Appendix C: Study Design Matrix

5 framings × 3 lengths × 7 domains = 105 prompts per model × 2 models = 210 total responses

| | Q1 Soil | Q2 Fert. | Q3 Pest | Q4 Cover | Q5 Comp. | Q6 Water | Q7 No-till |
|---|---|---|---|---|---|---|---|
| **N-S** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **N-M** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **N-L** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **NOV-S** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **NOV-M** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **NOV-L** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **MOD-S** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **MOD-M** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **MOD-L** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **EXP-S** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **EXP-M** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **EXP-L** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **PRO-S** | Yes | Refusal* | Yes | Yes | Yes | Yes | Error† |
| **PRO-M** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **PRO-L** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

*Q2-PRO-S (Claude): Full refusal retained in analysis with CC = 5, RS = 1
†Q7-PRO-S (Claude): No content generated — excluded from all analysis
