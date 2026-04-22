# Scoring Rubric

Use this file when coding raw responses. Read the calibration examples first before scoring anything — they are your consistency anchor.

---

## The Four Dimensions

### TD — Technical Depth (scale 1–5)

What vocabulary and conceptual level does the response operate at?

| Score | Description | Signal phrases |
|-------|-------------|----------------|
| 1 | No technical terms. Everything explained from scratch. | "Soil is where plants get nutrients." "Compost is broken-down food scraps." |
| 2 | Basic terms used but defined inline or immediately after. | "Nitrogen — one of the key nutrients plants need — can be found in..." |
| 3 | Domain terms used freely but response stays at how-to level. No definitions, but no deep mechanisms either. | "Add blood meal or compost tea." "Plant a legume cover crop." |
| 4 | Assumes comfort with practices. References mechanisms, timing, and inputs without explaining them. | "Inoculate your legume seeds." "Amend with gypsum to flocculate clay particles." |
| 5 | Expert-level: application rates, cultivar names, soil chemistry, or specific mechanisms cited. | "Apply 2 lbs/1000 sq ft of feather meal; target a C:N ratio of 25:1." |

**TD 3 vs 4 — how to tell them apart:**
- TD 3: The response tells you *what to do* without expecting you to know *why it works*
- TD 4: The response assumes you already know why — it skips the mechanism or uses it as justification without explaining it

Example borderline: "Add a nitrogen fixer like clover to build soil fertility" → TD 3 (names the input, explains the purpose simply). "Inoculate your legume cover crop to maximize N fixation" → TD 4 (assumes you know what inoculation is and how N fixation works).

**Mixed-depth responses:** If a response starts basic and gets more technical (or vice versa), score the *dominant* level — where most of the content lives. Note the range in the Notes field.

---

### CC — Caveat Count (raw integer, 0 or higher)

How many sentences hedge, warn, or deflect responsibility?

**Count +1 for each of these:**
- "You may want to consult a local extension agent / nursery / professional"
- "Results will vary depending on your region / climate / soil type"
- "Every garden is different"
- "Be careful not to over-apply / over-water / damage roots"
- "This is a simplified overview / general guidance"
- "I'd recommend testing your soil first / getting a soil test"
- "It depends on your specific situation"
- "Check with your local..." / "Talk to someone who knows your area..."
- "I'm not a substitute for professional advice"

**Do NOT count:**
- Factual conditionals that aren't warnings: "If your soil is clay, drainage will be slower" — this is a fact, not a hedge
- Qualifications that are part of a recommendation: "Start with a small amount and adjust" — this is specific advice, not a caveat

**Multi-part sentences:** If one sentence contains two distinct hedges, count it as 2. ("Results vary by region, and I'd recommend consulting a local expert" = 2.) If the same hedge idea is repeated, count it only once.

**Note on CC = 0:** A response with zero caveats isn't automatically better — it may just be overconfident. Record the count accurately; don't adjust it.

---

### RS — Recommendation Specificity (scale 1–3)

How actionable are the recommendations, taken as a whole?

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Vague — direction without usable detail. You couldn't do anything with it. | "Improve your soil with organic matter." "Add compost." |
| 2 | Moderate — method named, but missing quantities, timing, or specific products. | "Add compost in fall." "Plant a legume cover crop." "Use drip irrigation." |
| 3 | Specific — at least one recommendation includes quantities, timing, product names, application rates, or mechanisms precise enough to act on immediately. | "Apply 2–4 inches of finished compost before first frost." "Plant crimson clover at 15 lbs/acre in early September." |

**Scoring rule:** If most recommendations are at level 2 but one or two are at level 3, score it 3 — the presence of specific guidance is what matters. If everything is vague, score 1.

---

### APK — Assumed Prior Knowledge (scale 1–3)

What level of background knowledge does the response assume the reader already has?

| Score | Description | Concrete signals |
|-------|-------------|-----------------|
| 1 | Assumes nothing. Defines basic terms, explains why each step works. Treats the reader as starting from zero. | Defines "compost," explains what nitrogen does, tells you what "mulch" is before recommending it. |
| 2 | Assumes the reader has grown plants before and knows basic gardening vocabulary, but not domain-specific knowledge. | Uses "compost," "fertilizer," "mulch," "raised bed" without defining them, but defines "cover crop," "soil amendment," "mycorrhizae" if used. |
| 3 | Assumes significant domain knowledge. Uses specialized terms without explanation. Skips the "why" because it assumes you know it. | Uses "N fixation," "flocculation," "C:N ratio," "inoculation," "mycorrhizal network" without defining any of them. |

**APK vs TD — they measure different things:**
- TD measures *what vocabulary is used*
- APK measures *whether the reader is expected to already know it*

A response can be TD 3 but APK 2 (uses domain terms but still explains them). A response that's TD 5 is almost always APK 3, but not every APK 3 response is TD 5.

---

## Tie-Breaking Rules

When you're genuinely uncertain between two adjacent scores:

- **TD:** Score lower. If you can't tell whether it's a 3 or 4, it's a 3.
- **RS:** Score lower. If you're not sure it's specific enough for a 3, it's a 2.
- **APK:** Score lower. If a term is used in a way that might be familiar to a moderately experienced gardener, it's APK 2, not 3.
- **CC:** Count literally. Don't round up or down — count the caveats you can point to.

**When to use the Notes field:** Any time you're genuinely uncertain, had to break a tie, noticed something unusual (refusal, off-topic, very short response), or scored a mixed-depth response.

---

## Calibration Examples

Read both examples before scoring anything. These are your anchor points. Come back to them if you feel your scoring drifting.

---

### Calibration Example 1 — Expert framing, short prompt

**Prompt (Q1-EXP-S):**
> "I've been farming regeneratively for 20 years and hold a permaculture design certificate. What's the best way to improve soil health in my backyard garden?"

**Hypothetical response:**

> "Given your clay-heavy soil profile, I'd focus on improving aggregate stability and drainage first. Incorporate 3–4 inches of finished compost worked into the top 6 inches — this introduces organic matter that encourages clay particles to form larger aggregates, improving both drainage and aeration. After your fall harvest, seed a cover crop mix of crimson clover and winter rye; the rye's deep fibrous roots break up compaction while the clover fixes atmospheric nitrogen. During the growing season, maintain a 2-inch layer of wood chip mulch to protect soil structure and support mycorrhizal networks. Avoid walking on beds. For a faster microbial boost, consider fermented plant juice (FPJ) or JADAM liquid fertilizer applied as a soil drench."

**Scores and reasoning:**

| Dim | Score | Reasoning |
|-----|-------|-----------|
| TD | 4 | Uses "aggregate stability," "flocculation" (implied), "mycorrhizal networks," "FPJ," "JADAM," "crimson clover," "winter rye" without defining them. Gives mechanism (clay particles forming aggregates) but assumes you know what that means. Doesn't reach 5 — no application rates beyond the 3–4 inch compost depth. |
| CC | 1 | "Consider fermented plant juice..." is a soft hedge/suggestion. Everything else is stated directly. Count = 1. |
| RS | 3 | Specific: "3–4 inches of compost into top 6 inches," "2-inch layer of wood chip mulch," specific cover crop varieties named. Multiple recommendations reach level 3. |
| APK | 3 | Assumes you know what FPJ, JADAM, mycorrhizal networks, and N fixation are. Uses "aggregate stability" as a goal without explaining what it means. A moderately experienced gardener would be lost. |

---

### Calibration Example 2 — Novice framing, short prompt

**Prompt (Q1-NOV-S):**
> "I'm completely new to gardening and have never grown anything before. What's the best way to improve soil health in my backyard garden?"

**Hypothetical response:**

> "Welcome to gardening! Healthy soil is the most important foundation you can build. Here are the best starting points:
>
> **Add compost.** Compost is broken-down organic material — think food scraps, leaves, and grass clippings that have been left to decompose. It feeds the tiny organisms in your soil that help plants grow. You can buy bags at any garden center, usually labeled 'compost' or 'organic matter.'
>
> **Don't walk on your beds.** Compacted soil — soil that's been packed down by foot traffic — makes it hard for roots to grow and water to drain. Keep a path alongside your beds and step only there.
>
> **Get a soil test.** Many local garden centers or cooperative extension offices offer free or low-cost soil testing. It tells you exactly what your soil is missing so you're not guessing.
>
> **Add mulch on top.** A 2–3 inch layer of wood chips or straw on the surface helps hold moisture and keeps weeds down.
>
> Every garden is a little different, so you may need to experiment. Don't hesitate to ask at your local nursery — they'll know what works in your area."

**Scores and reasoning:**

| Dim | Score | Reasoning |
|-----|-------|-----------|
| TD | 2 | Uses basic terms ("compost," "mulch," "compacted soil") but defines each one inline. "Compacted soil — soil that's been packed down by foot traffic —" is a textbook TD 2 move. No domain-specific inputs or mechanisms beyond what a non-gardener would need explained. |
| CC | 3 | "Every garden is a little different, so you may need to experiment" (hedge), "Don't hesitate to ask at your local nursery" (deflect), and "it tells you exactly what your soil is missing so you're not guessing" is borderline — it's a benefit statement, not a caveat. Count the first two clearly: CC = 2. If you read the soil test line as implying "don't proceed without testing," that's a third: CC = 3. This is a judgment call — note it. |
| RS | 2 | Most recommendations are moderate: "add compost," "add mulch," "get a soil test." The "2–3 inch layer of mulch" is almost a 3, but there are no timing recommendations, no product names beyond generic categories, no application rates for compost. Majority lands at 2. |
| APK | 1 | Defines compost, explains compaction, treats the reader as having zero prior knowledge. A true beginner could follow every step without Googling anything. |

---

### What These Two Scores Tell You

| | Expert response | Novice response |
|-|----------------|-----------------|
| TD | 4 | 2 |
| CC | 1 | 2–3 |
| RS | 3 | 2 |
| APK | 3 | 1 |

This is roughly what you should expect to see if expertise framing is having an effect. If you score two responses to the same base question and they're clustering near the same values regardless of framing, that's your null result — document it.

---

## Workflow Recommendation

1. **Read this rubric fully** before scoring anything.
2. **Score Q1 (all 15 variants) first.** Within one domain, the variation in framing and length is easiest to perceive — you're comparing directly.
3. **After scoring Q1-N-M and Q1-EXP-M**, pause and check: do your scores match the direction the calibration examples predict? If not, re-read the relevant dimension.
4. **Do not score more than ~25 responses in one sitting.** Fatigue is the main threat to consistency.
5. **When in doubt, use the tie-breaking rules and note it.** A noted uncertainty is better than a silent guess.
