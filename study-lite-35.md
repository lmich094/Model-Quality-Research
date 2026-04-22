# AI Framing Study — Lite Version (35 Prompts)

This is the streamlined version of the full study. It isolates **one variable only: expertise framing**. Prompt length is held constant at a standard medium length (~75–130 words) across all prompts.

For the full study with prompt length as a second variable (105 prompts total), see `README.md`.

---

## Research Question

Does claiming expertise (or lack thereof) change the advice AI models give on regenerative and sustainable backyard farming?

## Design

- **7 base questions** covering key sustainable farming domains
- **5 framing levels** per question
- **1 fixed length** (medium — enough context to produce a substantive response)
- **Total: 35 prompts** per model tested

## Framing Levels

| Code | Prefix Added to Each Prompt |
|------|-----------------------------|
| **N** (Neutral) | *(no prefix)* |
| **NOV** (Novice) | "I'm completely new to gardening and have never grown anything before." |
| **MOD** (Moderate) | "I've been gardening for a couple of years but I'm still learning." |
| **EXP** (Expert) | "I've been farming regeneratively for 20 years and hold a permaculture design certificate." |
| **PRO** (Professional) | "I'm a professional agronomist with a background in soil science." |

## How to Run

1. Open a **fresh conversation** for every prompt — no shared context between prompts.
2. Paste each prompt exactly as written.
3. Do not tell the model it is being tested.
4. Record the full response and score it using the rubric below.

## Scoring Rubric

Score each response on four dimensions independently, before comparing responses.

**TD — Technical Depth (1–5)**
- 1: No technical terms; explains everything from first principles
- 2: Basic terms used but defined inline
- 3: Domain terms used without always defining them
- 4: Assumes familiarity with practices and inputs
- 5: Expert-level: specific rates, cultivars, mechanisms, scientific terminology

**CC — Caveat Count (raw count)**
Count sentences that hedge, warn, or deflect: "consult an expert," "results may vary," "every garden is different," "be careful not to...," etc.

**RS — Recommendation Specificity (1–3)**
- 1: Vague — direction without usable detail ("add organic matter")
- 2: Moderate — method named, no quantities or timing ("add compost in fall")
- 3: Specific — quantities, timing, or product names given ("apply 2–4 inches of compost before first frost")

**APK — Assumed Prior Knowledge (1–3)**
- 1: Explains everything from first principles
- 2: Assumes basic gardening familiarity
- 3: Assumes significant domain expertise; skips fundamentals

## Results Template

| Prompt ID | Model | Framing | Word Count (Response) | TD | CC | RS | APK | Notes |
|-----------|-------|---------|----------------------|----|----|----|-----|-------|
| Q1-N | | N | | | | | | |
| Q1-NOV | | NOV | | | | | | |
| Q1-MOD | | MOD | | | | | | |
| Q1-EXP | | EXP | | | | | | |
| Q1-PRO | | PRO | | | | | | |
| Q2-N | | N | | | | | | |
| ... | | | | | | | | |

---

## The 35 Prompts

Organized by question. Run all 5 variations of each question before moving to the next.

---

### Question 1: Soil Health

**Q1-N** | Neutral

> My garden is about 400 square feet and has been in the same spot for three years. The soil is dense and clay-heavy, and water tends to pool after heavy rain. I grow mostly tomatoes, zucchini, and leafy greens. What's the best way to improve soil health in my backyard garden?

---

**Q1-NOV** | Novice

> I'm completely new to gardening and have never grown anything before. My garden is about 400 square feet and has been in the same spot for three years. The soil is dense and clay-heavy, and water tends to pool after heavy rain. I grow mostly tomatoes, zucchini, and leafy greens. What's the best way to improve soil health in my backyard garden?

---

**Q1-MOD** | Moderate

> I've been gardening for a couple of years but I'm still learning. My garden is about 400 square feet and has been in the same spot for three years. The soil is dense and clay-heavy, and water tends to pool after heavy rain. I grow mostly tomatoes, zucchini, and leafy greens. What's the best way to improve soil health in my backyard garden?

---

**Q1-EXP** | Expert

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. My garden is about 400 square feet and has been in the same spot for three years. The soil is dense and clay-heavy, and water tends to pool after heavy rain. I grow mostly tomatoes, zucchini, and leafy greens. What's the best way to improve soil health in my backyard garden?

---

**Q1-PRO** | Professional

> I'm a professional agronomist with a background in soil science. My garden is about 400 square feet and has been in the same spot for three years. The soil is dense and clay-heavy, and water tends to pool after heavy rain. I grow mostly tomatoes, zucchini, and leafy greens. What's the best way to improve soil health in my backyard garden?

---
---

### Question 2: Fertilizer

**Q2-N** | Neutral

> I have two 4x8 foot raised beds where I grow vegetables from spring through fall. My plants look decent most years but yields feel lower than they should be, especially for tomatoes and peppers. I want to make a more informed decision about what to add to the soil this season. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-NOV** | Novice

> I'm completely new to gardening and have never grown anything before. I have two 4x8 foot raised beds where I grow vegetables from spring through fall. My plants look decent most years but yields feel lower than they should be, especially for tomatoes and peppers. I want to make a more informed decision about what to add to the soil this season. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-MOD** | Moderate

> I've been gardening for a couple of years but I'm still learning. I have two 4x8 foot raised beds where I grow vegetables from spring through fall. My plants look decent most years but yields feel lower than they should be, especially for tomatoes and peppers. I want to make a more informed decision about what to add to the soil this season. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-EXP** | Expert

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. I have two 4x8 foot raised beds where I grow vegetables from spring through fall. My plants look decent most years but yields feel lower than they should be, especially for tomatoes and peppers. I want to make a more informed decision about what to add to the soil this season. Should I use compost or synthetic fertilizer for my vegetable beds?

---

**Q2-PRO** | Professional

> I'm a professional agronomist with a background in soil science. I have two 4x8 foot raised beds where I grow vegetables from spring through fall. My plants look decent most years but yields feel lower than they should be, especially for tomatoes and peppers. I want to make a more informed decision about what to add to the soil this season. Should I use compost or synthetic fertilizer for my vegetable beds?

---
---

### Question 3: Pest Control

**Q3-N** | Neutral

> Last summer I lost most of my kale and cabbage to what I think were caterpillars, and my tomatoes had a significant aphid problem by August. I have young children and a dog who use the yard regularly, so I'm not comfortable using chemical pesticides. I need something that actually works. How do I deal with pests in my garden without using pesticides?

---

**Q3-NOV** | Novice

> I'm completely new to gardening and have never grown anything before. Last summer I lost most of my kale and cabbage to what I think were caterpillars, and my tomatoes had a significant aphid problem by August. I have young children and a dog who use the yard regularly, so I'm not comfortable using chemical pesticides. I need something that actually works. How do I deal with pests in my garden without using pesticides?

---

**Q3-MOD** | Moderate

> I've been gardening for a couple of years but I'm still learning. Last summer I lost most of my kale and cabbage to what I think were caterpillars, and my tomatoes had a significant aphid problem by August. I have young children and a dog who use the yard regularly, so I'm not comfortable using chemical pesticides. I need something that actually works. How do I deal with pests in my garden without using pesticides?

---

**Q3-EXP** | Expert

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. Last summer I lost most of my kale and cabbage to what I think were caterpillars, and my tomatoes had a significant aphid problem by August. I have young children and a dog who use the yard regularly, so I'm not comfortable using chemical pesticides. I need something that actually works. How do I deal with pests in my garden without using pesticides?

---

**Q3-PRO** | Professional

> I'm a professional agronomist with a background in soil science. Last summer I lost most of my kale and cabbage to what I think were caterpillars, and my tomatoes had a significant aphid problem by August. I have young children and a dog who use the yard regularly, so I'm not comfortable using chemical pesticides. I need something that actually works. How do I deal with pests in my garden without using pesticides?

---
---

### Question 4: Cover Crops

**Q4-N** | Neutral

> I have a 300 square foot vegetable garden in the Northeast that I'm putting to bed after fall harvest. The beds have been producing for two years and I've noticed the soil is getting more compacted. I want to use the winter to improve things for spring planting. What cover crops should I plant to improve my soil over winter?

---

**Q4-NOV** | Novice

> I'm completely new to gardening and have never grown anything before. I have a 300 square foot vegetable garden in the Northeast that I'm putting to bed after fall harvest. The beds have been producing for two years and I've noticed the soil is getting more compacted. I want to use the winter to improve things for spring planting. What cover crops should I plant to improve my soil over winter?

---

**Q4-MOD** | Moderate

> I've been gardening for a couple of years but I'm still learning. I have a 300 square foot vegetable garden in the Northeast that I'm putting to bed after fall harvest. The beds have been producing for two years and I've noticed the soil is getting more compacted. I want to use the winter to improve things for spring planting. What cover crops should I plant to improve my soil over winter?

---

**Q4-EXP** | Expert

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. I have a 300 square foot vegetable garden in the Northeast that I'm putting to bed after fall harvest. The beds have been producing for two years and I've noticed the soil is getting more compacted. I want to use the winter to improve things for spring planting. What cover crops should I plant to improve my soil over winter?

---

**Q4-PRO** | Professional

> I'm a professional agronomist with a background in soil science. I have a 300 square foot vegetable garden in the Northeast that I'm putting to bed after fall harvest. The beds have been producing for two years and I've noticed the soil is getting more compacted. I want to use the winter to improve things for spring planting. What cover crops should I plant to improve my soil over winter?

---
---

### Question 5: Composting

**Q5-N** | Neutral

> I have a decent amount of kitchen scraps and yard waste — vegetable peels, coffee grounds, grass clippings, leaves — and feel like I should be doing something useful with them. I have a medium-sized backyard with space along a fence line. I've never composted before and I'm not sure where to start. How do I set up a simple composting system at home?

---

**Q5-NOV** | Novice

> I'm completely new to gardening and have never grown anything before. I have a decent amount of kitchen scraps and yard waste — vegetable peels, coffee grounds, grass clippings, leaves — and feel like I should be doing something useful with them. I have a medium-sized backyard with space along a fence line. I've never composted before and I'm not sure where to start. How do I set up a simple composting system at home?

---

**Q5-MOD** | Moderate

> I've been gardening for a couple of years but I'm still learning. I have a decent amount of kitchen scraps and yard waste — vegetable peels, coffee grounds, grass clippings, leaves — and feel like I should be doing something useful with them. I have a medium-sized backyard with space along a fence line. I've never composted before and I'm not sure where to start. How do I set up a simple composting system at home?

---

**Q5-EXP** | Expert

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. I have a decent amount of kitchen scraps and yard waste — vegetable peels, coffee grounds, grass clippings, leaves — and feel like I should be doing something useful with them. I have a medium-sized backyard with space along a fence line. I've never composted before and I'm not sure where to start. How do I set up a simple composting system at home?

---

**Q5-PRO** | Professional

> I'm a professional agronomist with a background in soil science. I have a decent amount of kitchen scraps and yard waste — vegetable peels, coffee grounds, grass clippings, leaves — and feel like I should be doing something useful with them. I have a medium-sized backyard with space along a fence line. I've never composted before and I'm not sure where to start. How do I set up a simple composting system at home?

---
---

### Question 6: Water Conservation

**Q6-N** | Neutral

> I live in an area with hot, dry summers, and I'm currently watering my 500 square foot vegetable garden by hand almost every day. My water bill spikes noticeably from June through September. I want to find realistic ways to use less water without my plants suffering. What's the best way to conserve water in a backyard garden?

---

**Q6-NOV** | Novice

> I'm completely new to gardening and have never grown anything before. I live in an area with hot, dry summers, and I'm currently watering my 500 square foot vegetable garden by hand almost every day. My water bill spikes noticeably from June through September. I want to find realistic ways to use less water without my plants suffering. What's the best way to conserve water in a backyard garden?

---

**Q6-MOD** | Moderate

> I've been gardening for a couple of years but I'm still learning. I live in an area with hot, dry summers, and I'm currently watering my 500 square foot vegetable garden by hand almost every day. My water bill spikes noticeably from June through September. I want to find realistic ways to use less water without my plants suffering. What's the best way to conserve water in a backyard garden?

---

**Q6-EXP** | Expert

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. I live in an area with hot, dry summers, and I'm currently watering my 500 square foot vegetable garden by hand almost every day. My water bill spikes noticeably from June through September. I want to find realistic ways to use less water without my plants suffering. What's the best way to conserve water in a backyard garden?

---

**Q6-PRO** | Professional

> I'm a professional agronomist with a background in soil science. I live in an area with hot, dry summers, and I'm currently watering my 500 square foot vegetable garden by hand almost every day. My water bill spikes noticeably from June through September. I want to find realistic ways to use less water without my plants suffering. What's the best way to conserve water in a backyard garden?

---
---

### Question 7: No-Till Garden Setup

**Q7-N** | Neutral

> I have a 10x12 foot patch of lawn in my backyard that I want to convert into a vegetable garden. I don't want to till or dig the whole area up by hand. I've heard about no-till methods and they sound appealing but I don't know how to actually get started. How do I start a no-till garden bed from scratch?

---

**Q7-NOV** | Novice

> I'm completely new to gardening and have never grown anything before. I have a 10x12 foot patch of lawn in my backyard that I want to convert into a vegetable garden. I don't want to till or dig the whole area up by hand. I've heard about no-till methods and they sound appealing but I don't know how to actually get started. How do I start a no-till garden bed from scratch?

---

**Q7-MOD** | Moderate

> I've been gardening for a couple of years but I'm still learning. I have a 10x12 foot patch of lawn in my backyard that I want to convert into a vegetable garden. I don't want to till or dig the whole area up by hand. I've heard about no-till methods and they sound appealing but I don't know how to actually get started. How do I start a no-till garden bed from scratch?

---

**Q7-EXP** | Expert

> I've been farming regeneratively for 20 years and hold a permaculture design certificate. I have a 10x12 foot patch of lawn in my backyard that I want to convert into a vegetable garden. I don't want to till or dig the whole area up by hand. I've heard about no-till methods and they sound appealing but I don't know how to actually get started. How do I start a no-till garden bed from scratch?

---

**Q7-PRO** | Professional

> I'm a professional agronomist with a background in soil science. I have a 10x12 foot patch of lawn in my backyard that I want to convert into a vegetable garden. I don't want to till or dig the whole area up by hand. I've heard about no-till methods and they sound appealing but I don't know how to actually get started. How do I start a no-till garden bed from scratch?

---

## Prompt Count Summary

| Question | Domain | Prompts |
|----------|--------|---------|
| Q1 | Soil Health | 5 |
| Q2 | Fertilizer | 5 |
| Q3 | Pest Control | 5 |
| Q4 | Cover Crops | 5 |
| Q5 | Composting | 5 |
| Q6 | Water Conservation | 5 |
| Q7 | No-Till Garden Setup | 5 |
| **Total** | | **35** |

---

*Lite version of the full 105-prompt study. See `README.md` for the complete design including prompt length as a second variable.*
