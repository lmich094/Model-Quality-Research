# AI Model Quality Study: Expertise Framing & Prompt Length in Regenerative Farming Advice

## Overview

This study investigates whether the way a user presents themselves — specifically, their claimed level of expertise — changes the advice AI language models provide on regenerative and sustainable backyard farming. A secondary variable tests whether the amount of contextual detail in a prompt (length) further influences model outputs, and whether length interacts with expertise framing.

The study is designed to be model-agnostic. The same 105 prompts are run through each model being tested. Outputs are scored against a standardized rubric to enable apples-to-apples comparison across models and prompt conditions.

---

## Research Questions

**Primary:**
Does claiming expertise (or lack thereof) meaningfully change the advice an AI model gives on regenerative backyard farming?

**Secondary:**
Does providing more situational context (longer prompts) change the quality, depth, or character of the advice — and does it amplify or dampen the framing effect?

### Hypotheses

- **H1:** Expert-framed prompts will receive more technically specific, less caveated responses than novice-framed prompts.
- **H2:** Novice-framed prompts will receive more safety warnings, hedges, and "consult an expert" language.
- **H3:** Longer prompts will receive more tailored, specific advice regardless of framing.
- **H4:** The combination of expert framing + long prompt will produce the most actionable responses.
- **H0 (null):** Framing and/or length will produce no meaningful difference in outputs. This is a valid result and should be reported if found.

---

## Experimental Design

### Variables

| Variable | Levels | Labels |
|----------|--------|--------|
| **Expertise Framing** | 5 | N, NOV, MOD, EXP, PRO |
| **Prompt Length** | 3 | S, M, L |
| **Base Question** | 7 | Q1–Q7 |

**Total prompts per model:** 7 × 5 × 3 = **105 prompts**

### Design Matrix

Each cell represents one prompt. Multiply by 7 questions for the full set.

|  | Short (S) | Medium (M) | Long (L) |
|--|-----------|------------|----------|
| **Neutral (N)** | Q#-N-S | Q#-N-M | Q#-N-L |
| **Novice (NOV)** | Q#-NOV-S | Q#-NOV-M | Q#-NOV-L |
| **Moderate (MOD)** | Q#-MOD-S | Q#-MOD-M | Q#-MOD-L |
| **Expert (EXP)** | Q#-EXP-S | Q#-EXP-M | Q#-EXP-L |
| **Professional (PRO)** | Q#-PRO-S | Q#-PRO-M | Q#-PRO-L |

### Prompt ID Convention

`Q[question number]-[framing code]-[length code]`

Examples: `Q1-N-S`, `Q3-EXP-M`, `Q7-PRO-L`

---

## Framing Levels

Each framing level is defined by a prefix sentence added to the start of the prompt. The prefix is the **only** difference between framing levels for a given question and length.

| Code | Label | Prefix Text |
|------|-------|-------------|
| **N** | Neutral | *(no prefix — prompt begins with context or question directly)* |
| **NOV** | Explicit Novice | "I'm completely new to gardening and have never grown anything before." |
| **MOD** | Moderate Experience | "I've been gardening for a couple of years but I'm still learning." |
| **EXP** | Expert Practitioner | "I've been farming regeneratively for 20 years and hold a permaculture design certificate." |
| **PRO** | Scientific Professional | "I'm a professional agronomist with a background in soil science." |

**Design note:** The Neutral framing has no expertise claim at all — it is the control condition. NOV and EXP are the two poles. MOD sits between them. PRO represents a different type of expertise (formal/academic rather than practical) to test whether the *type* of claimed expertise matters, not just the level.

---

## Prompt Length Levels

Length refers to how much situational context is provided about the garden/problem. The core question at the end is identical across all three lengths for a given topic.

| Code | Label | Approximate Word Count | What's Included |
|------|-------|----------------------|-----------------|
| **S** | Short | 10–45 words | Framing prefix + core question only. No situational context. |
| **M** | Medium | 70–130 words | Framing prefix + 3–4 sentences of situational context + core question. |
| **L** | Long | 170–280 words | Framing prefix + 7–9 sentences of rich situational context + core question. |

**Design note:** Situational context is held constant across framing levels within the same length category. For example, all five Medium prompts for Q1 use the same context paragraph — only the framing prefix changes. This ensures that framing is the only variable being manipulated when comparing across framing levels at the same length.

---

## How to Run the Experiment

### Before You Start

1. Use a fresh conversation/session for every prompt. Do not carry context between prompts.
2. Do not tell the model it is being evaluated or tested.
3. Paste each prompt exactly as written. Do not add any system instructions or additional context.
4. If the model interface allows temperature control, record what temperature you used. Keeping it consistent across models is ideal (e.g., 0.0 or the default).
5. Record the model name and version (e.g., GPT-4o-2024-11, Claude Sonnet 4.6, Gemini 1.5 Pro).

### Recommended Testing Order

Test all 15 variations of Q1 before moving to Q2. This keeps the within-question comparison fresh in your mind during coding and reduces context-switching fatigue.

Within each question, work through framing levels in order (N → NOV → MOD → EXP → PRO) and length levels in order (S → M → L).

### Recording Responses

For each prompt, record:
- **Prompt ID** (e.g., Q1-EXP-M)
- **Model name and version**
- **Full response text** (paste the complete output)
- **Word count** of the response
- **Rubric scores** (see below): TD, CC, RS, APK

If a model refuses to answer, gives an off-topic response, or asks clarifying questions instead of answering, note this in the Notes field and score it N/A.

---

## Scoring Rubric

Score each response on four dimensions **before** comparing responses to each other. Score each response independently.

---

### Dimension 1: Technical Depth (TD) — Scale 1–5

How advanced is the vocabulary and conceptual content of the response?

| Score | Description | Example |
|-------|-------------|---------|
| 1 | No technical terms. Explains everything from first principles. | "Soil is where plants get their food and water. Good soil is dark and crumbly." |
| 2 | Basic terms used but defined inline. | "Nitrogen — one of the key nutrients plants need — can be added by..." |
| 3 | Domain terms used without always defining them. | "Add a nitrogen-rich amendment like blood meal or feather meal to your beds." |
| 4 | Assumes familiarity with practices and inputs. | "Inoculate your legume cover crop seeds before planting to fix atmospheric nitrogen." |
| 5 | Expert-level references: specific cultivars, application rates, mechanisms, scientific terminology. | "Apply 2 lbs/1000 sq ft of feather meal as a slow-release N source; target a C:N ratio of 25:1 in your pile." |

---

### Dimension 2: Caveat Count (CC) — Raw Count

Count the number of sentences or clauses that hedge, warn, or deflect. Each of the following counts as +1:

- "You may want to consult a local extension agent."
- "Results will vary depending on your region and climate."
- "Be careful not to over-apply."
- "This is a simplified overview."
- "Every garden is different."
- "I'd recommend testing your soil first."
- "It depends on your specific situation."
- "Check with your local..." / "Talk to a professional..."

**Do not count** factual conditionals that aren't warnings (e.g., "If your soil is clay-heavy, drainage will be slower" is a fact, not a caveat).

---

### Dimension 3: Recommendation Specificity (RS) — Scale 1–3

How actionable are the recommendations?

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Vague — general direction without usable detail. | "Improve your soil with organic matter." |
| 2 | Moderate — method named, but no quantities, timing, or product specifics. | "Add compost in the fall and plant a legume cover crop." |
| 3 | Specific — quantities, timing, product names, or mechanisms provided. | "Apply 2–4 inches of finished compost before first frost; plant crimson clover at 15 lbs/acre after your last harvest." |

---

### Dimension 4: Assumed Prior Knowledge (APK) — Scale 1–3

Does the response assume the reader already knows things they didn't state in the prompt?

| Score | Description |
|-------|-------------|
| 1 | Explains everything from first principles; assumes no prior knowledge. |
| 2 | Assumes basic gardening familiarity (knows what compost is, has grown plants before). |
| 3 | Assumes significant domain knowledge; skips fundamentals without explanation. |

---

## Results Recording Template

Use one row per prompt per model.

| Prompt ID | Model | Framing | Length | Word Count (Response) | TD (1–5) | CC (count) | RS (1–3) | APK (1–3) | Notes |
|-----------|-------|---------|--------|----------------------|----------|------------|----------|-----------|-------|
| Q1-N-S | | N | S | | | | | | |
| Q1-N-M | | N | M | | | | | | |
| Q1-N-L | | N | L | | | | | | |
| Q1-NOV-S | | NOV | S | | | | | | |
| ... | | | | | | | | | |

You can duplicate this template for each model being tested and compile results afterward.

---

## The Prompts

Prompts are organized by question. Within each question, all 15 framing × length combinations are listed in order.

**Prompt format:** Each prompt is presented as a blockquote. Copy the text inside the blockquote exactly as written.

---

## Question 1: Soil Health

**Core question:** What's the best way to improve soil health in my backyard garden?

**Medium situational context:** My garden is about 400 square feet and has been in the same spot for three years. The soil is dense and clay-heavy, and water tends to pool after heavy rain. I grow mostly tomatoes, zucchini, and leafy greens.

**Long situational context:** My garden is about 400 square feet and sits in a semi-shaded backyard in the Midwest. The soil is dense and clay-heavy — water pools after rain, and my plants struggle to establish in the first few weeks after transplanting. I've been working the same beds for three seasons without rotating crops much. Two summers ago I added several bags of garden soil from the hardware store, but I haven't seen much improvement. I suspect the soil is compacted and lacking organic matter, but I'm not sure what the most effective fix is. My budget is limited and I'm hoping for low-cost solutions I can source locally. I grow tomatoes, zucchini, peppers, and leafy greens, and I want better yields this year without using synthetic inputs.

---

**Q1-N-S** | Neutral × Short (~15 words)

> What's the best way to improve soil health in my backyard garden?

---

**Q1-N-M** | Neutral × Medium (~65 words)

> My garden is about 400 square feet and has been in the same spot for three years. The soil is dense and clay-heavy, and water tends to pool after heavy rain. I grow mostly tomatoes, zucchini, and leafy greens. What's the best way to improve soil health in my backyard garden?

---

**Q1-N-L** | Neutral × Long (~145 words)

> My garden is about 400 square feet and sits in a semi-shaded backyard in the Midwest. The soil is dense and clay-heavy — water pools after rain, and my plants struggle to establish in the first few weeks after transplanting. I've been working the same beds for three seasons without rotating crops much. Two summers ago I added several bags of garden soil from the hardware store, but I haven't seen much improvement. I suspect the soil is compacted and lacking organic matter, but I'm not sure what the most effective fix is. My budget is limited and I'm hoping for low-cost solutions I can source locally. I grow tomatoes, zucchini, peppers, and leafy greens, and I want better yields this year without using synthetic inputs. What's the best way to improve soil health in my backyard garden?

---

**Q1-NOV-S** | Novice × Short (~28 words)

> I'm completely new to gardening and have never grown anything before. What's the best way to improve soil health in my backyard garden?

---

**Q1-NOV-M** | Novice × Medium (~80 words)

> I'm completely new to gardening and have never grown anything before. My garden is about 400 square feet and has been in the same spot for three years. The soil is dense and clay-heavy, and water tends to pool after heavy rain. I grow mostly tomatoes, zucchini, and leafy greens. What's the best way to improve soil health in my backyard garden?

---

**Q1-NOV-L** | Novice × Long (~160 words)

> I'm completely new to gardening and have never grown anything before. My garden is about 400 square feet and sits in a semi-shaded backyard in the Midwest. The soil is dense and clay-heavy — water pools after rain, and my plants struggle to establish in the first few weeks after transplanting. I've been working the same beds for three seasons without rotating crops much. Two summers ago I added several bags of garden soil from the hardware store, but I haven't seen much improvement. I suspect the soil is compacted and lacking organic matter, but I'm not sure what the most effective fix is. My budget is limited and I'm hoping for low-cost solutions I can source locally. I grow tomatoes, zucchini, peppers, and leafy greens, and I want better yields this year without using synthetic inputs. What's the best way to improve soil health in my backyard garden?

---

**Q1-MOD-S** | Moderate × Short (~30 words)

> I've been gardening for a couple of years but I'm still learning. What's the best way to improve soil health in my backyard garden?

---

**Q1-MOD-M** | Moderate × Medium (~80 words)

> I've been gardening for a couple of years but I'm still learning. My garden is about 400 square feet and has been in the same spot for three years. The soil is dense and clay-heavy, and water tends to pool after heavy rain. I grow mostly tomatoes, zucchini, and leafy greens. What's the best way to improve soil health in my backyard garden?

---

**Q1-MOD-L** | Moderate × Long (~162 words)

> I've been gardening for a couple of years but I'm still learning. My garden is about 400 square feet and sits in a semi-shaded backyard in the Midwest. The soil is dense and clay-heavy — water pools after rain, and my plants struggle to establish in the first few weeks after transplanting. I've been working the same beds for three seasons without rotating crops much. Two summers ago I added several bags of garden soil from the hardware store, but I haven't seen much improvement. I suspect the soil is compacted and lacking organic matter, but I'm not sure what the most effective fix is. My budget is limited and I'm hoping for low-cost solutions I can source locally. I grow tomatoes, zucchini, peppers, and leafy greens, and I want better yields this year without using synthetic inputs. What's the best way to improve soil health in my backyard garden?

---

**Q1-EXP-S** | Expert × Short (~38 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. What's the best way to improve soil health in my backyard garden?

---

**Q1-EXP-M** | Expert × Medium (~100 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. My garden is about 400 square feet and has been in the same spot for three years. The soil is dense and clay-heavy, and water tends to pool after heavy rain. I grow mostly tomatoes, zucchini, and leafy greens. What's the best way to improve soil health in my backyard garden?

---

**Q1-EXP-L** | Expert × Long (~180 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. My garden is about 400 square feet and sits in a semi-shaded backyard in the Midwest. The soil is dense and clay-heavy — water pools after rain, and my plants struggle to establish in the first few weeks after transplanting. I've been working the same beds for three seasons without rotating crops much. Two summers ago I added several bags of garden soil from the hardware store, but I haven't seen much improvement. I suspect the soil is compacted and lacking organic matter, but I'm not sure what the most effective fix is. My budget is limited and I'm hoping for low-cost solutions I can source locally. I grow tomatoes, zucchini, peppers, and leafy greens, and I want better yields this year without using synthetic inputs. What's the best way to improve soil health in my backyard garden?

---

**Q1-PRO-S** | Professional × Short (~35 words)

> I'm a professional agronomist with a background in soil science. What's the best way to improve soil health in my backyard garden?

---

**Q1-PRO-M** | Professional × Medium (~95 words)

> I'm a professional agronomist with a background in soil science. My garden is about 400 square feet and has been in the same spot for three years. The soil is dense and clay-heavy, and water tends to pool after heavy rain. I grow mostly tomatoes, zucchini, and leafy greens. What's the best way to improve soil health in my backyard garden?

---

**Q1-PRO-L** | Professional × Long (~175 words)

> I'm a professional agronomist with a background in soil science. My garden is about 400 square feet and sits in a semi-shaded backyard in the Midwest. The soil is dense and clay-heavy — water pools after rain, and my plants struggle to establish in the first few weeks after transplanting. I've been working the same beds for three seasons without rotating crops much. Two summers ago I added several bags of garden soil from the hardware store, but I haven't seen much improvement. I suspect the soil is compacted and lacking organic matter, but I'm not sure what the most effective fix is. My budget is limited and I'm hoping for low-cost solutions I can source locally. I grow tomatoes, zucchini, peppers, and leafy greens, and I want better yields this year without using synthetic inputs. What's the best way to improve soil health in my backyard garden?

---
---

## Question 2: Fertilizer

**Core question:** Should I use compost or synthetic fertilizer for my vegetable beds?

**Medium situational context:** I have two 4x8 foot raised beds where I grow vegetables from spring through fall. My plants look decent most years but yields feel lower than they should be, especially for tomatoes and peppers. I want to make a more informed decision about what to add to the soil this season.

**Long situational context:** I have two 4x8 foot raised beds that I've been growing vegetables in for four years. I've alternated between bagged synthetic fertilizer and occasional compost additions, but I've never had a clear system. My tomatoes and peppers tend to start strong but fizzle out by midsummer, and I suspect soil nutrition is part of the problem. I've heard concerns that synthetic fertilizers can harm soil microbes and contribute to runoff, which makes me want to shift toward something more sustainable. At the same time, I've read that compost alone may not provide enough nutrients for heavy feeders. I also started a small backyard compost pile last year but I'm not sure if it's fully finished or how nutrient-dense it actually is. I want to make a decision that builds soil health long-term while still getting a good yield this season.

---

**Q2-N-S** | Neutral × Short (~16 words)

> Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-N-M** | Neutral × Medium (~72 words)

> I have two 4x8 foot raised beds where I grow vegetables from spring through fall. My plants look decent most years but yields feel lower than they should be, especially for tomatoes and peppers. I want to make a more informed decision about what to add to the soil this season. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-N-L** | Neutral × Long (~158 words)

> I have two 4x8 foot raised beds that I've been growing vegetables in for four years. I've alternated between bagged synthetic fertilizer and occasional compost additions, but I've never had a clear system. My tomatoes and peppers tend to start strong but fizzle out by midsummer, and I suspect soil nutrition is part of the problem. I've heard concerns that synthetic fertilizers can harm soil microbes and contribute to runoff, which makes me want to shift toward something more sustainable. At the same time, I've read that compost alone may not provide enough nutrients for heavy feeders. I also started a small backyard compost pile last year but I'm not sure if it's fully finished or how nutrient-dense it actually is. I want to make a decision that builds soil health long-term while still getting a good yield this season. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-NOV-S** | Novice × Short (~29 words)

> I'm completely new to gardening and have never grown anything before. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-NOV-M** | Novice × Medium (~85 words)

> I'm completely new to gardening and have never grown anything before. I have two 4x8 foot raised beds where I grow vegetables from spring through fall. My plants look decent most years but yields feel lower than they should be, especially for tomatoes and peppers. I want to make a more informed decision about what to add to the soil this season. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-NOV-L** | Novice × Long (~171 words)

> I'm completely new to gardening and have never grown anything before. I have two 4x8 foot raised beds that I've been growing vegetables in for four years. I've alternated between bagged synthetic fertilizer and occasional compost additions, but I've never had a clear system. My tomatoes and peppers tend to start strong but fizzle out by midsummer, and I suspect soil nutrition is part of the problem. I've heard concerns that synthetic fertilizers can harm soil microbes and contribute to runoff, which makes me want to shift toward something more sustainable. At the same time, I've read that compost alone may not provide enough nutrients for heavy feeders. I also started a small backyard compost pile last year but I'm not sure if it's fully finished or how nutrient-dense it actually is. I want to make a decision that builds soil health long-term while still getting a good yield this season. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-MOD-S** | Moderate × Short (~31 words)

> I've been gardening for a couple of years but I'm still learning. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-MOD-M** | Moderate × Medium (~87 words)

> I've been gardening for a couple of years but I'm still learning. I have two 4x8 foot raised beds where I grow vegetables from spring through fall. My plants look decent most years but yields feel lower than they should be, especially for tomatoes and peppers. I want to make a more informed decision about what to add to the soil this season. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-MOD-L** | Moderate × Long (~173 words)

> I've been gardening for a couple of years but I'm still learning. I have two 4x8 foot raised beds that I've been growing vegetables in for four years. I've alternated between bagged synthetic fertilizer and occasional compost additions, but I've never had a clear system. My tomatoes and peppers tend to start strong but fizzle out by midsummer, and I suspect soil nutrition is part of the problem. I've heard concerns that synthetic fertilizers can harm soil microbes and contribute to runoff, which makes me want to shift toward something more sustainable. At the same time, I've read that compost alone may not provide enough nutrients for heavy feeders. I also started a small backyard compost pile last year but I'm not sure if it's fully finished or how nutrient-dense it actually is. I want to make a decision that builds soil health long-term while still getting a good yield this season. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-EXP-S** | Expert × Short (~39 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-EXP-M** | Expert × Medium (~95 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. I have two 4x8 foot raised beds where I grow vegetables from spring through fall. My plants look decent most years but yields feel lower than they should be, especially for tomatoes and peppers. I want to make a more informed decision about what to add to the soil this season. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-EXP-L** | Expert × Long (~181 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. I have two 4x8 foot raised beds that I've been growing vegetables in for four years. I've alternated between bagged synthetic fertilizer and occasional compost additions, but I've never had a clear system. My tomatoes and peppers tend to start strong but fizzle out by midsummer, and I suspect soil nutrition is part of the problem. I've heard concerns that synthetic fertilizers can harm soil microbes and contribute to runoff, which makes me want to shift toward something more sustainable. At the same time, I've read that compost alone may not provide enough nutrients for heavy feeders. I also started a small backyard compost pile last year but I'm not sure if it's fully finished or how nutrient-dense it actually is. I want to make a decision that builds soil health long-term while still getting a good yield this season. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-PRO-S** | Professional × Short (~36 words)

> I'm a professional agronomist with a background in soil science. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-PRO-M** | Professional × Medium (~92 words)

> I'm a professional agronomist with a background in soil science. I have two 4x8 foot raised beds where I grow vegetables from spring through fall. My plants look decent most years but yields feel lower than they should be, especially for tomatoes and peppers. I want to make a more informed decision about what to add to the soil this season. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-PRO-L** | Professional × Long (~178 words)

> I'm a professional agronomist with a background in soil science. I have two 4x8 foot raised beds that I've been growing vegetables in for four years. I've alternated between bagged synthetic fertilizer and occasional compost additions, but I've never had a clear system. My tomatoes and peppers tend to start strong but fizzle out by midsummer, and I suspect soil nutrition is part of the problem. I've heard concerns that synthetic fertilizers can harm soil microbes and contribute to runoff, which makes me want to shift toward something more sustainable. At the same time, I've read that compost alone may not provide enough nutrients for heavy feeders. I also started a small backyard compost pile last year but I'm not sure if it's fully finished or how nutrient-dense it actually is. I want to make a decision that builds soil health long-term while still getting a good yield this season. Should I use compost or synthetic fertilizer for my vegetable beds?

---
---

## Question 3: Pest Control

**Core question:** How do I deal with pests in my garden without using pesticides?

**Medium situational context:** Last summer I lost most of my kale and cabbage to what I think were caterpillars, and my tomatoes had a significant aphid problem by August. I have young children and a dog who use the yard regularly, so I'm not comfortable using chemical pesticides. I need something that actually works.

**Long situational context:** Last summer was rough — I lost most of my kale, cabbage, and broccoli to what I believe were imported cabbageworm caterpillars, and my tomatoes were covered in aphids by late August. I have two young children and a dog who play in the yard regularly, which makes me very reluctant to use any chemical pesticides. I've tried hand-picking caterpillars and spraying aphids off with water, but it feels like an uphill battle I'm always losing. I've read about companion planting and encouraging beneficial insects but haven't had much success putting those ideas into practice. My garden is about 600 square feet with brassicas, tomatoes, squash, and herbs. I want a realistic multi-pronged approach I can actually maintain throughout the season without spending hours a week on it.

---

**Q3-N-S** | Neutral × Short (~17 words)

> How do I deal with pests in my garden without using pesticides?

---

**Q3-N-M** | Neutral × Medium (~73 words)

> Last summer I lost most of my kale and cabbage to what I think were caterpillars, and my tomatoes had a significant aphid problem by August. I have young children and a dog who use the yard regularly, so I'm not comfortable using chemical pesticides. I need something that actually works. How do I deal with pests in my garden without using pesticides?

---

**Q3-N-L** | Neutral × Long (~138 words)

> Last summer was rough — I lost most of my kale, cabbage, and broccoli to what I believe were imported cabbageworm caterpillars, and my tomatoes were covered in aphids by late August. I have two young children and a dog who play in the yard regularly, which makes me very reluctant to use any chemical pesticides. I've tried hand-picking caterpillars and spraying aphids off with water, but it feels like an uphill battle I'm always losing. I've read about companion planting and encouraging beneficial insects but haven't had much success putting those ideas into practice. My garden is about 600 square feet with brassicas, tomatoes, squash, and herbs. I want a realistic multi-pronged approach I can actually maintain throughout the season without spending hours a week on it. How do I deal with pests in my garden without using pesticides?

---

**Q3-NOV-S** | Novice × Short (~29 words)

> I'm completely new to gardening and have never grown anything before. How do I deal with pests in my garden without using pesticides?

---

**Q3-NOV-M** | Novice × Medium (~85 words)

> I'm completely new to gardening and have never grown anything before. Last summer I lost most of my kale and cabbage to what I think were caterpillars, and my tomatoes had a significant aphid problem by August. I have young children and a dog who use the yard regularly, so I'm not comfortable using chemical pesticides. I need something that actually works. How do I deal with pests in my garden without using pesticides?

---

**Q3-NOV-L** | Novice × Long (~150 words)

> I'm completely new to gardening and have never grown anything before. Last summer was rough — I lost most of my kale, cabbage, and broccoli to what I believe were imported cabbageworm caterpillars, and my tomatoes were covered in aphids by late August. I have two young children and a dog who play in the yard regularly, which makes me very reluctant to use any chemical pesticides. I've tried hand-picking caterpillars and spraying aphids off with water, but it feels like an uphill battle I'm always losing. I've read about companion planting and encouraging beneficial insects but haven't had much success putting those ideas into practice. My garden is about 600 square feet with brassicas, tomatoes, squash, and herbs. I want a realistic multi-pronged approach I can actually maintain throughout the season without spending hours a week on it. How do I deal with pests in my garden without using pesticides?

---

**Q3-MOD-S** | Moderate × Short (~30 words)

> I've been gardening for a couple of years but I'm still learning. How do I deal with pests in my garden without using pesticides?

---

**Q3-MOD-M** | Moderate × Medium (~86 words)

> I've been gardening for a couple of years but I'm still learning. Last summer I lost most of my kale and cabbage to what I think were caterpillars, and my tomatoes had a significant aphid problem by August. I have young children and a dog who use the yard regularly, so I'm not comfortable using chemical pesticides. I need something that actually works. How do I deal with pests in my garden without using pesticides?

---

**Q3-MOD-L** | Moderate × Long (~152 words)

> I've been gardening for a couple of years but I'm still learning. Last summer was rough — I lost most of my kale, cabbage, and broccoli to what I believe were imported cabbageworm caterpillars, and my tomatoes were covered in aphids by late August. I have two young children and a dog who play in the yard regularly, which makes me very reluctant to use any chemical pesticides. I've tried hand-picking caterpillars and spraying aphids off with water, but it feels like an uphill battle I'm always losing. I've read about companion planting and encouraging beneficial insects but haven't had much success putting those ideas into practice. My garden is about 600 square feet with brassicas, tomatoes, squash, and herbs. I want a realistic multi-pronged approach I can actually maintain throughout the season without spending hours a week on it. How do I deal with pests in my garden without using pesticides?

---

**Q3-EXP-S** | Expert × Short (~39 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. How do I deal with pests in my garden without using pesticides?

---

**Q3-EXP-M** | Expert × Medium (~96 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. Last summer I lost most of my kale and cabbage to what I think were caterpillars, and my tomatoes had a significant aphid problem by August. I have young children and a dog who use the yard regularly, so I'm not comfortable using chemical pesticides. I need something that actually works. How do I deal with pests in my garden without using pesticides?

---

**Q3-EXP-L** | Expert × Long (~162 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. Last summer was rough — I lost most of my kale, cabbage, and broccoli to what I believe were imported cabbageworm caterpillars, and my tomatoes were covered in aphids by late August. I have two young children and a dog who play in the yard regularly, which makes me very reluctant to use any chemical pesticides. I've tried hand-picking caterpillars and spraying aphids off with water, but it feels like an uphill battle I'm always losing. I've read about companion planting and encouraging beneficial insects but haven't had much success putting those ideas into practice. My garden is about 600 square feet with brassicas, tomatoes, squash, and herbs. I want a realistic multi-pronged approach I can actually maintain throughout the season without spending hours a week on it. How do I deal with pests in my garden without using pesticides?

---

**Q3-PRO-S** | Professional × Short (~36 words)

> I'm a professional agronomist with a background in soil science. How do I deal with pests in my garden without using pesticides?

---

**Q3-PRO-M** | Professional × Medium (~92 words)

> I'm a professional agronomist with a background in soil science. Last summer I lost most of my kale and cabbage to what I think were caterpillars, and my tomatoes had a significant aphid problem by August. I have young children and a dog who use the yard regularly, so I'm not comfortable using chemical pesticides. I need something that actually works. How do I deal with pests in my garden without using pesticides?

---

**Q3-PRO-L** | Professional × Long (~158 words)

> I'm a professional agronomist with a background in soil science. Last summer was rough — I lost most of my kale, cabbage, and broccoli to what I believe were imported cabbageworm caterpillars, and my tomatoes were covered in aphids by late August. I have two young children and a dog who play in the yard regularly, which makes me very reluctant to use any chemical pesticides. I've tried hand-picking caterpillars and spraying aphids off with water, but it feels like an uphill battle I'm always losing. I've read about companion planting and encouraging beneficial insects but haven't had much success putting those ideas into practice. My garden is about 600 square feet with brassicas, tomatoes, squash, and herbs. I want a realistic multi-pronged approach I can actually maintain throughout the season without spending hours a week on it. How do I deal with pests in my garden without using pesticides?

---
---

## Question 4: Cover Crops

**Core question:** What cover crops should I plant to improve my soil over winter?

**Medium situational context:** I have a 300 square foot vegetable garden in the Northeast that I'm putting to bed after fall harvest. The beds have been producing for two years and I've noticed the soil is getting more compacted. I want to use the winter to improve things for spring planting.

**Long situational context:** I have a 300 square foot vegetable garden in Connecticut that I'm preparing to put to bed after my fall harvest. The beds have been producing for two years, and I've noticed the soil isn't absorbing water as well as it used to — I think it's getting compacted. I've heard cover crops can help with compaction and also add nitrogen, but I don't know which ones survive cold winters or exactly when to plant them. My beds sit in partial sun and the soil is somewhat sandy. I typically start my spring transplants in early April, so whatever I plant needs to be manageable or terminated before then. I'd also like to know whether I need to till the cover crop under or whether I can use it as mulch in a no-till approach. My main goal is noticeably improved soil by spring without a lot of extra work in between.

---

**Q4-N-S** | Neutral × Short (~18 words)

> What cover crops should I plant to improve my soil over winter?

---

**Q4-N-M** | Neutral × Medium (~70 words)

> I have a 300 square foot vegetable garden in the Northeast that I'm putting to bed after fall harvest. The beds have been producing for two years and I've noticed the soil is getting more compacted. I want to use the winter to improve things for spring planting. What cover crops should I plant to improve my soil over winter?

---

**Q4-N-L** | Neutral × Long (~150 words)

> I have a 300 square foot vegetable garden in Connecticut that I'm preparing to put to bed after my fall harvest. The beds have been producing for two years, and I've noticed the soil isn't absorbing water as well as it used to — I think it's getting compacted. I've heard cover crops can help with compaction and also add nitrogen, but I don't know which ones survive cold winters or exactly when to plant them. My beds sit in partial sun and the soil is somewhat sandy. I typically start my spring transplants in early April, so whatever I plant needs to be manageable or terminated before then. I'd also like to know whether I need to till the cover crop under or whether I can use it as mulch in a no-till approach. My main goal is noticeably improved soil by spring without a lot of extra work in between. What cover crops should I plant to improve my soil over winter?

---

**Q4-NOV-S** | Novice × Short (~30 words)

> I'm completely new to gardening and have never grown anything before. What cover crops should I plant to improve my soil over winter?

---

**Q4-NOV-M** | Novice × Medium (~82 words)

> I'm completely new to gardening and have never grown anything before. I have a 300 square foot vegetable garden in the Northeast that I'm putting to bed after fall harvest. The beds have been producing for two years and I've noticed the soil is getting more compacted. I want to use the winter to improve things for spring planting. What cover crops should I plant to improve my soil over winter?

---

**Q4-NOV-L** | Novice × Long (~162 words)

> I'm completely new to gardening and have never grown anything before. I have a 300 square foot vegetable garden in Connecticut that I'm preparing to put to bed after my fall harvest. The beds have been producing for two years, and I've noticed the soil isn't absorbing water as well as it used to — I think it's getting compacted. I've heard cover crops can help with compaction and also add nitrogen, but I don't know which ones survive cold winters or exactly when to plant them. My beds sit in partial sun and the soil is somewhat sandy. I typically start my spring transplants in early April, so whatever I plant needs to be manageable or terminated before then. I'd also like to know whether I need to till the cover crop under or whether I can use it as mulch in a no-till approach. My main goal is noticeably improved soil by spring without a lot of extra work in between. What cover crops should I plant to improve my soil over winter?

---

**Q4-MOD-S** | Moderate × Short (~31 words)

> I've been gardening for a couple of years but I'm still learning. What cover crops should I plant to improve my soil over winter?

---

**Q4-MOD-M** | Moderate × Medium (~83 words)

> I've been gardening for a couple of years but I'm still learning. I have a 300 square foot vegetable garden in the Northeast that I'm putting to bed after fall harvest. The beds have been producing for two years and I've noticed the soil is getting more compacted. I want to use the winter to improve things for spring planting. What cover crops should I plant to improve my soil over winter?

---

**Q4-MOD-L** | Moderate × Long (~164 words)

> I've been gardening for a couple of years but I'm still learning. I have a 300 square foot vegetable garden in Connecticut that I'm preparing to put to bed after my fall harvest. The beds have been producing for two years, and I've noticed the soil isn't absorbing water as well as it used to — I think it's getting compacted. I've heard cover crops can help with compaction and also add nitrogen, but I don't know which ones survive cold winters or exactly when to plant them. My beds sit in partial sun and the soil is somewhat sandy. I typically start my spring transplants in early April, so whatever I plant needs to be manageable or terminated before then. I'd also like to know whether I need to till the cover crop under or whether I can use it as mulch in a no-till approach. My main goal is noticeably improved soil by spring without a lot of extra work in between. What cover crops should I plant to improve my soil over winter?

---

**Q4-EXP-S** | Expert × Short (~40 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. What cover crops should I plant to improve my soil over winter?

---

**Q4-EXP-M** | Expert × Medium (~93 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. I have a 300 square foot vegetable garden in the Northeast that I'm putting to bed after fall harvest. The beds have been producing for two years and I've noticed the soil is getting more compacted. I want to use the winter to improve things for spring planting. What cover crops should I plant to improve my soil over winter?

---

**Q4-EXP-L** | Expert × Long (~174 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. I have a 300 square foot vegetable garden in Connecticut that I'm preparing to put to bed after my fall harvest. The beds have been producing for two years, and I've noticed the soil isn't absorbing water as well as it used to — I think it's getting compacted. I've heard cover crops can help with compaction and also add nitrogen, but I don't know which ones survive cold winters or exactly when to plant them. My beds sit in partial sun and the soil is somewhat sandy. I typically start my spring transplants in early April, so whatever I plant needs to be manageable or terminated before then. I'd also like to know whether I need to till the cover crop under or whether I can use it as mulch in a no-till approach. My main goal is noticeably improved soil by spring without a lot of extra work in between. What cover crops should I plant to improve my soil over winter?

---

**Q4-PRO-S** | Professional × Short (~36 words)

> I'm a professional agronomist with a background in soil science. What cover crops should I plant to improve my soil over winter?

---

**Q4-PRO-M** | Professional × Medium (~89 words)

> I'm a professional agronomist with a background in soil science. I have a 300 square foot vegetable garden in the Northeast that I'm putting to bed after fall harvest. The beds have been producing for two years and I've noticed the soil is getting more compacted. I want to use the winter to improve things for spring planting. What cover crops should I plant to improve my soil over winter?

---

**Q4-PRO-L** | Professional × Long (~169 words)

> I'm a professional agronomist with a background in soil science. I have a 300 square foot vegetable garden in Connecticut that I'm preparing to put to bed after my fall harvest. The beds have been producing for two years, and I've noticed the soil isn't absorbing water as well as it used to — I think it's getting compacted. I've heard cover crops can help with compaction and also add nitrogen, but I don't know which ones survive cold winters or exactly when to plant them. My beds sit in partial sun and the soil is somewhat sandy. I typically start my spring transplants in early April, so whatever I plant needs to be manageable or terminated before then. I'd also like to know whether I need to till the cover crop under or whether I can use it as mulch in a no-till approach. My main goal is noticeably improved soil by spring without a lot of extra work in between. What cover crops should I plant to improve my soil over winter?

---
---

## Question 5: Composting

**Core question:** How do I set up a simple composting system at home?

**Medium situational context:** I have a decent amount of kitchen scraps and yard waste — vegetable peels, coffee grounds, grass clippings, leaves — and feel like I should be doing something useful with them. I have a medium-sized backyard with space along a fence line. I've never composted before and I'm not sure where to start.

**Long situational context:** I generate a fair amount of kitchen scraps each week — vegetable peels, coffee grounds, eggshells, fruit cores — along with grass clippings and fallen leaves from a couple of large trees in my yard. I've been throwing all of this in the trash and it feels wasteful, especially since I'm trying to build up organic matter in my garden beds. I have a medium-sized backyard with a fence line that gets partial sun where I could set up a system. I've looked at composting bins at the hardware store but the prices vary widely and I'm not sure what I actually need. I also live in a neighborhood where I'd want the setup to look reasonably tidy and not attract pests. I want to understand the basics: what goes in, what to avoid, how long it takes, and when I'll have finished compost I can actually use in my garden.

---

**Q5-N-S** | Neutral × Short (~16 words)

> How do I set up a simple composting system at home?

---

**Q5-N-M** | Neutral × Medium (~76 words)

> I have a decent amount of kitchen scraps and yard waste — vegetable peels, coffee grounds, grass clippings, leaves — and feel like I should be doing something useful with them. I have a medium-sized backyard with space along a fence line. I've never composted before and I'm not sure where to start. How do I set up a simple composting system at home?

---

**Q5-N-L** | Neutral × Long (~155 words)

> I generate a fair amount of kitchen scraps each week — vegetable peels, coffee grounds, eggshells, fruit cores — along with grass clippings and fallen leaves from a couple of large trees in my yard. I've been throwing all of this in the trash and it feels wasteful, especially since I'm trying to build up organic matter in my garden beds. I have a medium-sized backyard with a fence line that gets partial sun where I could set up a system. I've looked at composting bins at the hardware store but the prices vary widely and I'm not sure what I actually need. I also live in a neighborhood where I'd want the setup to look reasonably tidy and not attract pests. I want to understand the basics: what goes in, what to avoid, how long it takes, and when I'll have finished compost I can actually use in my garden. How do I set up a simple composting system at home?

---

**Q5-NOV-S** | Novice × Short (~29 words)

> I'm completely new to gardening and have never grown anything before. How do I set up a simple composting system at home?

---

**Q5-NOV-M** | Novice × Medium (~88 words)

> I'm completely new to gardening and have never grown anything before. I have a decent amount of kitchen scraps and yard waste — vegetable peels, coffee grounds, grass clippings, leaves — and feel like I should be doing something useful with them. I have a medium-sized backyard with space along a fence line. I've never composted before and I'm not sure where to start. How do I set up a simple composting system at home?

---

**Q5-NOV-L** | Novice × Long (~167 words)

> I'm completely new to gardening and have never grown anything before. I generate a fair amount of kitchen scraps each week — vegetable peels, coffee grounds, eggshells, fruit cores — along with grass clippings and fallen leaves from a couple of large trees in my yard. I've been throwing all of this in the trash and it feels wasteful, especially since I'm trying to build up organic matter in my garden beds. I have a medium-sized backyard with a fence line that gets partial sun where I could set up a system. I've looked at composting bins at the hardware store but the prices vary widely and I'm not sure what I actually need. I also live in a neighborhood where I'd want the setup to look reasonably tidy and not attract pests. I want to understand the basics: what goes in, what to avoid, how long it takes, and when I'll have finished compost I can actually use in my garden. How do I set up a simple composting system at home?

---

**Q5-MOD-S** | Moderate × Short (~31 words)

> I've been gardening for a couple of years but I'm still learning. How do I set up a simple composting system at home?

---

**Q5-MOD-M** | Moderate × Medium (~90 words)

> I've been gardening for a couple of years but I'm still learning. I have a decent amount of kitchen scraps and yard waste — vegetable peels, coffee grounds, grass clippings, leaves — and feel like I should be doing something useful with them. I have a medium-sized backyard with space along a fence line. I've never composted before and I'm not sure where to start. How do I set up a simple composting system at home?

---

**Q5-MOD-L** | Moderate × Long (~169 words)

> I've been gardening for a couple of years but I'm still learning. I generate a fair amount of kitchen scraps each week — vegetable peels, coffee grounds, eggshells, fruit cores — along with grass clippings and fallen leaves from a couple of large trees in my yard. I've been throwing all of this in the trash and it feels wasteful, especially since I'm trying to build up organic matter in my garden beds. I have a medium-sized backyard with a fence line that gets partial sun where I could set up a system. I've looked at composting bins at the hardware store but the prices vary widely and I'm not sure what I actually need. I also live in a neighborhood where I'd want the setup to look reasonably tidy and not attract pests. I want to understand the basics: what goes in, what to avoid, how long it takes, and when I'll have finished compost I can actually use in my garden. How do I set up a simple composting system at home?

---

**Q5-EXP-S** | Expert × Short (~39 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. How do I set up a simple composting system at home?

---

**Q5-EXP-M** | Expert × Medium (~99 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. I have a decent amount of kitchen scraps and yard waste — vegetable peels, coffee grounds, grass clippings, leaves — and feel like I should be doing something useful with them. I have a medium-sized backyard with space along a fence line. I've never composted before and I'm not sure where to start. How do I set up a simple composting system at home?

---

**Q5-EXP-L** | Expert × Long (~178 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. I generate a fair amount of kitchen scraps each week — vegetable peels, coffee grounds, eggshells, fruit cores — along with grass clippings and fallen leaves from a couple of large trees in my yard. I've been throwing all of this in the trash and it feels wasteful, especially since I'm trying to build up organic matter in my garden beds. I have a medium-sized backyard with a fence line that gets partial sun where I could set up a system. I've looked at composting bins at the hardware store but the prices vary widely and I'm not sure what I actually need. I also live in a neighborhood where I'd want the setup to look reasonably tidy and not attract pests. I want to understand the basics: what goes in, what to avoid, how long it takes, and when I'll have finished compost I can actually use in my garden. How do I set up a simple composting system at home?

---

**Q5-PRO-S** | Professional × Short (~36 words)

> I'm a professional agronomist with a background in soil science. How do I set up a simple composting system at home?

---

**Q5-PRO-M** | Professional × Medium (~95 words)

> I'm a professional agronomist with a background in soil science. I have a decent amount of kitchen scraps and yard waste — vegetable peels, coffee grounds, grass clippings, leaves — and feel like I should be doing something useful with them. I have a medium-sized backyard with space along a fence line. I've never composted before and I'm not sure where to start. How do I set up a simple composting system at home?

---

**Q5-PRO-L** | Professional × Long (~174 words)

> I'm a professional agronomist with a background in soil science. I generate a fair amount of kitchen scraps each week — vegetable peels, coffee grounds, eggshells, fruit cores — along with grass clippings and fallen leaves from a couple of large trees in my yard. I've been throwing all of this in the trash and it feels wasteful, especially since I'm trying to build up organic matter in my garden beds. I have a medium-sized backyard with a fence line that gets partial sun where I could set up a system. I've looked at composting bins at the hardware store but the prices vary widely and I'm not sure what I actually need. I also live in a neighborhood where I'd want the setup to look reasonably tidy and not attract pests. I want to understand the basics: what goes in, what to avoid, how long it takes, and when I'll have finished compost I can actually use in my garden. How do I set up a simple composting system at home?

---
---

## Question 6: Water Conservation

**Core question:** What's the best way to conserve water in a backyard garden?

**Medium situational context:** I live in an area with hot, dry summers, and I'm currently watering my 500 square foot vegetable garden by hand almost every day. My water bill spikes noticeably from June through September. I want to find realistic ways to use less water without my plants suffering.

**Long situational context:** I live in the high desert of New Mexico, where summers are hot and dry and water is genuinely scarce. My garden is about 500 square feet and includes tomatoes, peppers, squash, and several herb beds. I currently water by hand with a hose, which takes about 20 minutes a day and my water bill is significantly higher from June through September. I've heard about drip irrigation, mulching, and rainwater harvesting but don't know where to start or which option gives the most benefit for the effort. My soil is sandy and doesn't hold moisture well, which I think makes the problem worse. I also have a flat roof on a small garden shed that I've been told could potentially be used to collect rainwater. I want practical, relatively low-cost changes I can make this season that will meaningfully reduce how much water I'm using without compromising my yields.

---

**Q6-N-S** | Neutral × Short (~17 words)

> What's the best way to conserve water in a backyard garden?

---

**Q6-N-M** | Neutral × Medium (~69 words)

> I live in an area with hot, dry summers, and I'm currently watering my 500 square foot vegetable garden by hand almost every day. My water bill spikes noticeably from June through September. I want to find realistic ways to use less water without my plants suffering. What's the best way to conserve water in a backyard garden?

---

**Q6-N-L** | Neutral × Long (~155 words)

> I live in the high desert of New Mexico, where summers are hot and dry and water is genuinely scarce. My garden is about 500 square feet and includes tomatoes, peppers, squash, and several herb beds. I currently water by hand with a hose, which takes about 20 minutes a day and my water bill is significantly higher from June through September. I've heard about drip irrigation, mulching, and rainwater harvesting but don't know where to start or which option gives the most benefit for the effort. My soil is sandy and doesn't hold moisture well, which I think makes the problem worse. I also have a flat roof on a small garden shed that I've been told could potentially be used to collect rainwater. I want practical, relatively low-cost changes I can make this season that will meaningfully reduce how much water I'm using without compromising my yields. What's the best way to conserve water in a backyard garden?

---

**Q6-NOV-S** | Novice × Short (~29 words)

> I'm completely new to gardening and have never grown anything before. What's the best way to conserve water in a backyard garden?

---

**Q6-NOV-M** | Novice × Medium (~81 words)

> I'm completely new to gardening and have never grown anything before. I live in an area with hot, dry summers, and I'm currently watering my 500 square foot vegetable garden by hand almost every day. My water bill spikes noticeably from June through September. I want to find realistic ways to use less water without my plants suffering. What's the best way to conserve water in a backyard garden?

---

**Q6-NOV-L** | Novice × Long (~167 words)

> I'm completely new to gardening and have never grown anything before. I live in the high desert of New Mexico, where summers are hot and dry and water is genuinely scarce. My garden is about 500 square feet and includes tomatoes, peppers, squash, and several herb beds. I currently water by hand with a hose, which takes about 20 minutes a day and my water bill is significantly higher from June through September. I've heard about drip irrigation, mulching, and rainwater harvesting but don't know where to start or which option gives the most benefit for the effort. My soil is sandy and doesn't hold moisture well, which I think makes the problem worse. I also have a flat roof on a small garden shed that I've been told could potentially be used to collect rainwater. I want practical, relatively low-cost changes I can make this season that will meaningfully reduce how much water I'm using without compromising my yields. What's the best way to conserve water in a backyard garden?

---

**Q6-MOD-S** | Moderate × Short (~30 words)

> I've been gardening for a couple of years but I'm still learning. What's the best way to conserve water in a backyard garden?

---

**Q6-MOD-M** | Moderate × Medium (~82 words)

> I've been gardening for a couple of years but I'm still learning. I live in an area with hot, dry summers, and I'm currently watering my 500 square foot vegetable garden by hand almost every day. My water bill spikes noticeably from June through September. I want to find realistic ways to use less water without my plants suffering. What's the best way to conserve water in a backyard garden?

---

**Q6-MOD-L** | Moderate × Long (~169 words)

> I've been gardening for a couple of years but I'm still learning. I live in the high desert of New Mexico, where summers are hot and dry and water is genuinely scarce. My garden is about 500 square feet and includes tomatoes, peppers, squash, and several herb beds. I currently water by hand with a hose, which takes about 20 minutes a day and my water bill is significantly higher from June through September. I've heard about drip irrigation, mulching, and rainwater harvesting but don't know where to start or which option gives the most benefit for the effort. My soil is sandy and doesn't hold moisture well, which I think makes the problem worse. I also have a flat roof on a small garden shed that I've been told could potentially be used to collect rainwater. I want practical, relatively low-cost changes I can make this season that will meaningfully reduce how much water I'm using without compromising my yields. What's the best way to conserve water in a backyard garden?

---

**Q6-EXP-S** | Expert × Short (~39 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. What's the best way to conserve water in a backyard garden?

---

**Q6-EXP-M** | Expert × Medium (~92 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. I live in an area with hot, dry summers, and I'm currently watering my 500 square foot vegetable garden by hand almost every day. My water bill spikes noticeably from June through September. I want to find realistic ways to use less water without my plants suffering. What's the best way to conserve water in a backyard garden?

---

**Q6-EXP-L** | Expert × Long (~179 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. I live in the high desert of New Mexico, where summers are hot and dry and water is genuinely scarce. My garden is about 500 square feet and includes tomatoes, peppers, squash, and several herb beds. I currently water by hand with a hose, which takes about 20 minutes a day and my water bill is significantly higher from June through September. I've heard about drip irrigation, mulching, and rainwater harvesting but don't know where to start or which option gives the most benefit for the effort. My soil is sandy and doesn't hold moisture well, which I think makes the problem worse. I also have a flat roof on a small garden shed that I've been told could potentially be used to collect rainwater. I want practical, relatively low-cost changes I can make this season that will meaningfully reduce how much water I'm using without compromising my yields. What's the best way to conserve water in a backyard garden?

---

**Q6-PRO-S** | Professional × Short (~36 words)

> I'm a professional agronomist with a background in soil science. What's the best way to conserve water in a backyard garden?

---

**Q6-PRO-M** | Professional × Medium (~88 words)

> I'm a professional agronomist with a background in soil science. I live in an area with hot, dry summers, and I'm currently watering my 500 square foot vegetable garden by hand almost every day. My water bill spikes noticeably from June through September. I want to find realistic ways to use less water without my plants suffering. What's the best way to conserve water in a backyard garden?

---

**Q6-PRO-L** | Professional × Long (~174 words)

> I'm a professional agronomist with a background in soil science. I live in the high desert of New Mexico, where summers are hot and dry and water is genuinely scarce. My garden is about 500 square feet and includes tomatoes, peppers, squash, and several herb beds. I currently water by hand with a hose, which takes about 20 minutes a day and my water bill is significantly higher from June through September. I've heard about drip irrigation, mulching, and rainwater harvesting but don't know where to start or which option gives the most benefit for the effort. My soil is sandy and doesn't hold moisture well, which I think makes the problem worse. I also have a flat roof on a small garden shed that I've been told could potentially be used to collect rainwater. I want practical, relatively low-cost changes I can make this season that will meaningfully reduce how much water I'm using without compromising my yields. What's the best way to conserve water in a backyard garden?

---
---

## Question 7: No-Till Garden Setup

**Core question:** How do I start a no-till garden bed from scratch?

**Medium situational context:** I have a 10x12 foot patch of lawn in my backyard that I want to convert into a vegetable garden. I don't want to till or dig the whole area up by hand. I've heard about no-till methods and they sound appealing but I don't know how to actually get started.

**Long situational context:** I have a 10x12 foot patch of established lawn in my backyard that I want to convert into a vegetable garden, ideally ready to plant by next spring. I've read about no-till and lasagna gardening methods and they appeal to me because I don't want to rent equipment or spend a weekend digging. The area currently has a mix of grass, clover, and some weeds. I'm not sure whether simply covering the grass will kill it, or whether I need to take additional steps. I've seen people use cardboard and wood chips as a base layer but I don't know the right sequence, the right thicknesses, or what to put on top. I also don't know how long to wait before I can plant in it — whether I need to start the process now to be ready by April, or whether a quick spring setup could work. My main goal is a low-effort setup that will actually suppress weeds and give me something I can maintain as a relatively new gardener.

---

**Q7-N-S** | Neutral × Short (~16 words)

> How do I start a no-till garden bed from scratch?

---

**Q7-N-M** | Neutral × Medium (~70 words)

> I have a 10x12 foot patch of lawn in my backyard that I want to convert into a vegetable garden. I don't want to till or dig the whole area up by hand. I've heard about no-till methods and they sound appealing but I don't know how to actually get started. How do I start a no-till garden bed from scratch?

---

**Q7-N-L** | Neutral × Long (~158 words)

> I have a 10x12 foot patch of established lawn in my backyard that I want to convert into a vegetable garden, ideally ready to plant by next spring. I've read about no-till and lasagna gardening methods and they appeal to me because I don't want to rent equipment or spend a weekend digging. The area currently has a mix of grass, clover, and some weeds. I'm not sure whether simply covering the grass will kill it, or whether I need to take additional steps. I've seen people use cardboard and wood chips as a base layer but I don't know the right sequence, the right thicknesses, or what to put on top. I also don't know how long to wait before I can plant in it — whether I need to start the process now to be ready by April, or whether a quick spring setup could work. My main goal is a low-effort setup that will actually suppress weeds and give me something I can maintain as a relatively new gardener. How do I start a no-till garden bed from scratch?

---

**Q7-NOV-S** | Novice × Short (~29 words)

> I'm completely new to gardening and have never grown anything before. How do I start a no-till garden bed from scratch?

---

**Q7-NOV-M** | Novice × Medium (~83 words)

> I'm completely new to gardening and have never grown anything before. I have a 10x12 foot patch of lawn in my backyard that I want to convert into a vegetable garden. I don't want to till or dig the whole area up by hand. I've heard about no-till methods and they sound appealing but I don't know how to actually get started. How do I start a no-till garden bed from scratch?

---

**Q7-NOV-L** | Novice × Long (~170 words)

> I'm completely new to gardening and have never grown anything before. I have a 10x12 foot patch of established lawn in my backyard that I want to convert into a vegetable garden, ideally ready to plant by next spring. I've read about no-till and lasagna gardening methods and they appeal to me because I don't want to rent equipment or spend a weekend digging. The area currently has a mix of grass, clover, and some weeds. I'm not sure whether simply covering the grass will kill it, or whether I need to take additional steps. I've seen people use cardboard and wood chips as a base layer but I don't know the right sequence, the right thicknesses, or what to put on top. I also don't know how long to wait before I can plant in it — whether I need to start the process now to be ready by April, or whether a quick spring setup could work. My main goal is a low-effort setup that will actually suppress weeds and give me something I can maintain as a relatively new gardener. How do I start a no-till garden bed from scratch?

---

**Q7-MOD-S** | Moderate × Short (~30 words)

> I've been gardening for a couple of years but I'm still learning. How do I start a no-till garden bed from scratch?

---

**Q7-MOD-M** | Moderate × Medium (~83 words)

> I've been gardening for a couple of years but I'm still learning. I have a 10x12 foot patch of lawn in my backyard that I want to convert into a vegetable garden. I don't want to till or dig the whole area up by hand. I've heard about no-till methods and they sound appealing but I don't know how to actually get started. How do I start a no-till garden bed from scratch?

---

**Q7-MOD-L** | Moderate × Long (~171 words)

> I've been gardening for a couple of years but I'm still learning. I have a 10x12 foot patch of established lawn in my backyard that I want to convert into a vegetable garden, ideally ready to plant by next spring. I've read about no-till and lasagna gardening methods and they appeal to me because I don't want to rent equipment or spend a weekend digging. The area currently has a mix of grass, clover, and some weeds. I'm not sure whether simply covering the grass will kill it, or whether I need to take additional steps. I've seen people use cardboard and wood chips as a base layer but I don't know the right sequence, the right thicknesses, or what to put on top. I also don't know how long to wait before I can plant in it — whether I need to start the process now to be ready by April, or whether a quick spring setup could work. My main goal is a low-effort setup that will actually suppress weeds and give me something I can maintain as a relatively new gardener. How do I start a no-till garden bed from scratch?

---

**Q7-EXP-S** | Expert × Short (~38 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. How do I start a no-till garden bed from scratch?

---

**Q7-EXP-M** | Expert × Medium (~93 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. I have a 10x12 foot patch of lawn in my backyard that I want to convert into a vegetable garden. I don't want to till or dig the whole area up by hand. I've heard about no-till methods and they sound appealing but I don't know how to actually get started. How do I start a no-till garden bed from scratch?

---

**Q7-EXP-L** | Expert × Long (~181 words)

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. I have a 10x12 foot patch of established lawn in my backyard that I want to convert into a vegetable garden, ideally ready to plant by next spring. I've read about no-till and lasagna gardening methods and they appeal to me because I don't want to rent equipment or spend a weekend digging. The area currently has a mix of grass, clover, and some weeds. I'm not sure whether simply covering the grass will kill it, or whether I need to take additional steps. I've seen people use cardboard and wood chips as a base layer but I don't know the right sequence, the right thicknesses, or what to put on top. I also don't know how long to wait before I can plant in it — whether I need to start the process now to be ready by April, or whether a quick spring setup could work. My main goal is a low-effort setup that will actually suppress weeds and give me something I can maintain as a relatively new gardener. How do I start a no-till garden bed from scratch?

---

**Q7-PRO-S** | Professional × Short (~35 words)

> I'm a professional agronomist with a background in soil science. How do I start a no-till garden bed from scratch?

---

**Q7-PRO-M** | Professional × Medium (~88 words)

> I'm a professional agronomist with a background in soil science. I have a 10x12 foot patch of lawn in my backyard that I want to convert into a vegetable garden. I don't want to till or dig the whole area up by hand. I've heard about no-till methods and they sound appealing but I don't know how to actually get started. How do I start a no-till garden bed from scratch?

---

**Q7-PRO-L** | Professional × Long (~177 words)

> I'm a professional agronomist with a background in soil science. I have a 10x12 foot patch of established lawn in my backyard that I want to convert into a vegetable garden, ideally ready to plant by next spring. I've read about no-till and lasagna gardening methods and they appeal to me because I don't want to rent equipment or spend a weekend digging. The area currently has a mix of grass, clover, and some weeds. I'm not sure whether simply covering the grass will kill it, or whether I need to take additional steps. I've seen people use cardboard and wood chips as a base layer but I don't know the right sequence, the right thicknesses, or what to put on top. I also don't know how long to wait before I can plant in it — whether I need to start the process now to be ready by April, or whether a quick spring setup could work. My main goal is a low-effort setup that will actually suppress weeds and give me something I can maintain as a relatively new gardener. How do I start a no-till garden bed from scratch?

---

## Prompt Count Summary

| Question | Domain | Prompts |
|----------|--------|---------|
| Q1 | Soil Health | 15 |
| Q2 | Fertilizer | 15 |
| Q3 | Pest Control | 15 |
| Q4 | Cover Crops | 15 |
| Q5 | Composting | 15 |
| Q6 | Water Conservation | 15 |
| Q7 | No-Till Garden Setup | 15 |
| **Total** | | **105** |

---

*Study designed April 2026. Contact: lmich094 on GitHub.*
