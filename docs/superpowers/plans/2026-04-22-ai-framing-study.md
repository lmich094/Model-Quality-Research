# AI Expertise Framing Study — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Determine whether claiming expertise (or lack of it) changes the advice AI models give on regenerative backyard farming questions.

**Architecture:** 7 base questions × 5 framing levels = 35 prompts, run through 1+ models at temperature 0 for reproducibility. Outputs hand-coded on a 4-dimension rubric. Results written up with null results as an acceptable outcome.

**Tech Stack:** Python 3, anthropic SDK, CSV for storage, manual rubric coding

---

## File Map

| File | Purpose |
|------|---------|
| `study/design.md` | Research question, hypotheses, definitions |
| `study/questions.json` | 7 base farming questions |
| `study/framings.json` | 5 framing variations with prefix text |
| `study/build_prompts.py` | Combines questions × framings → `prompts.json` |
| `study/prompts.json` | Generated: all 35 prompt objects |
| `study/rubric.md` | 4-dimension coding rubric with scoring rules |
| `study/run_experiment.py` | Calls the API, writes raw outputs to CSV |
| `study/results/raw/` | Raw CSV outputs per model run |
| `study/results/coding_sheet.csv` | Hand-coded rubric scores for all outputs |
| `study/analyze.py` | Aggregates coded scores, prints summary table |
| `study/report.md` | Final write-up |
| `.env` | API key (gitignored) |
| `.gitignore` | Excludes `.env` and raw outputs if desired |

---

### Task 1: Initialize Repo and Write Study Design

**Files:**
- Create: `study/design.md`

- [ ] **Step 1: Initialize git**

```bash
cd /home/liam_michka/regAg
git init
```

Expected: `Initialized empty Git repository in .../regAg/.git/`

- [ ] **Step 2: Write the study design**

Write `study/design.md`:

```markdown
# Study Design

## Research Question
Does user expertise framing meaningfully change the advice AI models give on
regenerative and sustainable backyard farming?

## Hypotheses
- **H1:** Expert-framed prompts will receive more technically specific, less caveated responses.
- **H2:** Novice-framed prompts will receive more basic recommendations with more
  safety warnings and "consult an expert" language.
- **H3:** The magnitude of this difference will vary across models.
- **H0 (null):** Framing will produce no meaningful difference in outputs.

## What Counts as "Meaningful"
A difference is meaningful if it changes the actionability of advice — if a novice
user following the expert response would be misled, or if an expert user following
the novice response would find the advice too vague to act on.

## Scope
- 7 base questions covering key sustainable farming domains
- 5 framing levels per question (35 prompts total)
- 1+ AI models, temperature 0.0 for reproducibility
- Manual coding against a 4-dimension rubric
```

- [ ] **Step 3: Commit**

```bash
git add study/design.md docs/
git commit -m "feat: initialize study repo with design and plan"
```

---

### Task 2: Write the Base Questions

**Files:**
- Create: `study/questions.json`

- [ ] **Step 1: Create the question bank**

Write `study/questions.json`:

```json
[
  {
    "id": "q1",
    "domain": "soil health",
    "question": "What's the best way to improve soil health in my backyard garden?"
  },
  {
    "id": "q2",
    "domain": "fertilizer",
    "question": "Should I use compost or synthetic fertilizer for my vegetable beds?"
  },
  {
    "id": "q3",
    "domain": "pest control",
    "question": "How do I deal with pests in my garden without using pesticides?"
  },
  {
    "id": "q4",
    "domain": "cover crops",
    "question": "What cover crops should I plant to improve my soil over winter?"
  },
  {
    "id": "q5",
    "domain": "composting",
    "question": "How do I set up a simple composting system at home?"
  },
  {
    "id": "q6",
    "domain": "water conservation",
    "question": "What's the best way to conserve water in a backyard garden?"
  },
  {
    "id": "q7",
    "domain": "no-till",
    "question": "How do I start a no-till garden bed from scratch?"
  }
]
```

- [ ] **Step 2: Commit**

```bash
git add study/questions.json
git commit -m "feat: add 7 base questions across key sustainable farming domains"
```

---

### Task 3: Write the Framing Variations and Build Prompts

**Files:**
- Create: `study/framings.json`
- Create: `study/build_prompts.py`
- Generate: `study/prompts.json`

- [ ] **Step 1: Create framing definitions**

Write `study/framings.json`:

```json
[
  {
    "id": "f1",
    "label": "neutral",
    "prefix": ""
  },
  {
    "id": "f2",
    "label": "explicit_novice",
    "prefix": "I'm completely new to gardening and have never grown anything before. "
  },
  {
    "id": "f3",
    "label": "moderate",
    "prefix": "I've been gardening for a couple of years but I'm still learning. "
  },
  {
    "id": "f4",
    "label": "expert",
    "prefix": "I've been farming regeneratively for 20 years and hold a permaculture design certificate. "
  },
  {
    "id": "f5",
    "label": "professional",
    "prefix": "I'm a professional agronomist advising a client on transitioning their backyard property. "
  }
]
```

- [ ] **Step 2: Write the prompt builder**

Write `study/build_prompts.py`:

```python
import json


def build_prompts(questions_path, framings_path):
    with open(questions_path) as f:
        questions = json.load(f)
    with open(framings_path) as f:
        framings = json.load(f)

    prompts = []
    for q in questions:
        for fr in framings:
            prompts.append({
                "id": f"{q['id']}_{fr['id']}",
                "question_id": q["id"],
                "framing_id": fr["id"],
                "framing_label": fr["label"],
                "domain": q["domain"],
                "text": fr["prefix"] + q["question"]
            })
    return prompts


if __name__ == "__main__":
    prompts = build_prompts("study/questions.json", "study/framings.json")
    with open("study/prompts.json", "w") as f:
        json.dump(prompts, f, indent=2)
    print(f"Built {len(prompts)} prompts")
```

- [ ] **Step 3: Run the builder**

```bash
python study/build_prompts.py
```

Expected output: `Built 35 prompts`

- [ ] **Step 4: Spot-check the output**

```bash
python -c "
import json
prompts = json.load(open('study/prompts.json'))
for p in [prompts[0], prompts[1], prompts[4]]:
    print(p['id'], '|', p['text'])
    print()
"
```

Verify: `q1_f1` has no prefix, `q1_f2` starts with "I'm completely new to gardening...", `q1_f5` starts with "I'm a professional agronomist..."

- [ ] **Step 5: Commit**

```bash
git add study/framings.json study/build_prompts.py study/prompts.json
git commit -m "feat: add 5 framing variations and prompt builder (35 prompts total)"
```

---

### Task 4: Define the Coding Rubric

**Files:**
- Create: `study/rubric.md`

- [ ] **Step 1: Write the rubric**

Write `study/rubric.md`:

```markdown
# Output Coding Rubric

Score each AI response on 4 dimensions. Score each response independently
before comparing across framings.

---

## Dimension 1: Technical Depth (TD) — scale 1–5

How advanced is the vocabulary and conceptual content?

- **1:** No technical terms. Everything explained from scratch.
  Example: "Soil is where plants grow and get their food."
- **2:** Basic terms used but defined inline.
  Example: "Nitrogen — one of the key nutrients plants need to grow — can be added with..."
- **3:** Domain terms used without always defining them.
  Example: "Add a nitrogen-rich amendment like blood meal or feather meal."
- **4:** Assumes familiarity with practices and inputs.
  Example: "Inoculate your legume cover crop seeds before planting to fix atmospheric nitrogen."
- **5:** Expert-level references: specific cultivars, application rates, mechanisms.
  Example: "Apply 2 lbs/1000 sq ft of feather meal as a slow-release N source; target a C:N ratio of 25:1 in your compost pile."

---

## Dimension 2: Caveat Count (CC) — raw count

Count the number of sentences that hedge, warn, or deflect responsibility.

Count each of these as +1:
- "You may want to consult a local extension agent."
- "Results will vary depending on your region and climate."
- "Be careful not to over-apply."
- "This is a simplified overview."
- "Every garden is different."
- "I'd recommend testing your soil first."
- "It depends on your specific situation."

Do not count factual conditionals ("If your soil is clay-heavy, ...") unless
they also contain a warning or hedge.

---

## Dimension 3: Recommendation Specificity (RS) — scale 1–3

How actionable are the recommendations?

- **1:** Vague — direction without detail.
  Example: "Improve your soil with organic matter."
- **2:** Moderate — method named, no quantities or timing.
  Example: "Add compost in the fall and plant a legume cover crop."
- **3:** Specific — quantities, timing, product names, or mechanisms given.
  Example: "Apply 2–4 inches of finished compost before first frost; plant crimson clover
  at 15 lbs/acre after your last harvest; terminate it 2–3 weeks before spring planting."

---

## Dimension 4: Assumed Prior Knowledge (APK) — scale 1–3

Does the response assume background knowledge the user didn't provide?

- **1:** Explains everything from first principles; assumes no prior knowledge.
- **2:** Assumes basic gardening familiarity (knows what compost is, has planted before).
- **3:** Assumes domain expertise; skips fundamentals without explanation.

---

## Also Record Per Row

| Field | What to record |
|-------|---------------|
| `word_count` | Auto-filled by runner |
| `TD` | Your score (1–5) |
| `CC` | Your count (0–N) |
| `RS` | Your score (1–3) |
| `APK` | Your score (1–3) |
| `notes` | Anything notable: unusual response, refusal, off-topic, etc. |
```

- [ ] **Step 2: Commit**

```bash
git add study/rubric.md
git commit -m "feat: add 4-dimension output coding rubric"
```

---

### Task 5: Set Up the API Runner

**Files:**
- Create: `.gitignore`
- Create: `.env`
- Create: `study/run_experiment.py`

- [ ] **Step 1: Create .gitignore**

Write `.gitignore`:

```
.env
__pycache__/
*.pyc
```

- [ ] **Step 2: Create .env placeholder**

Write `.env`:

```
ANTHROPIC_API_KEY=your_key_here
```

- [ ] **Step 3: Install dependencies**

```bash
pip install anthropic python-dotenv
```

Expected: `Successfully installed anthropic-...`

- [ ] **Step 4: Write the runner**

Write `study/run_experiment.py`:

```python
import csv
import json
import os
import sys
import time
from datetime import datetime

import anthropic
from dotenv import load_dotenv

load_dotenv()

MODELS = {
    "sonnet": "claude-sonnet-4-6",
    "opus": "claude-opus-4-7",
    "haiku": "claude-haiku-4-5-20251001",
}
TEMPERATURE = 0.0
MAX_TOKENS = 1024


def run_prompt(client, model_id, prompt_text):
    response = client.messages.create(
        model=model_id,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        messages=[{"role": "user", "content": prompt_text}],
    )
    return response.content[0].text


def main(model_key="sonnet", limit=None):
    if model_key not in MODELS:
        print(f"Unknown model '{model_key}'. Choose from: {list(MODELS.keys())}")
        sys.exit(1)

    model_id = MODELS[model_key]
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    with open("study/prompts.json") as f:
        prompts = json.load(f)

    if limit:
        prompts = prompts[:limit]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"study/results/raw/outputs_{model_key}_{timestamp}.csv"

    fieldnames = [
        "prompt_id", "question_id", "framing_id", "framing_label",
        "domain", "prompt_text", "response", "word_count", "model", "timestamp",
    ]

    with open(output_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i, prompt in enumerate(prompts):
            print(f"[{i+1}/{len(prompts)}] {prompt['id']} ({model_key})")
            response_text = run_prompt(client, model_id, prompt["text"])
            writer.writerow({
                "prompt_id": prompt["id"],
                "question_id": prompt["question_id"],
                "framing_id": prompt["framing_id"],
                "framing_label": prompt["framing_label"],
                "domain": prompt["domain"],
                "prompt_text": prompt["text"],
                "response": response_text,
                "word_count": len(response_text.split()),
                "model": model_id,
                "timestamp": datetime.now().isoformat(),
            })
            time.sleep(0.5)

    print(f"\nDone. {len(prompts)} responses saved to {output_path}")


if __name__ == "__main__":
    model_key = sys.argv[1] if len(sys.argv) > 1 else "sonnet"
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else None
    main(model_key, limit)
```

- [ ] **Step 5: Add your API key to .env**

Open `.env` and replace `your_key_here` with your actual Anthropic API key.

- [ ] **Step 6: Commit (without .env)**

```bash
git add .gitignore study/run_experiment.py
git commit -m "feat: add API runner supporting multiple models and pilot mode"
```

---

### Task 6: Pilot Run (5 Prompts)

Validate everything works before paying for 35 API calls.

- [ ] **Step 1: Run pilot (first 5 prompts, sonnet)**

```bash
python study/run_experiment.py sonnet 5
```

Expected output:
```
[1/5] q1_f1 (sonnet)
[2/5] q1_f2 (sonnet)
[3/5] q1_f3 (sonnet)
[4/5] q1_f4 (sonnet)
[5/5] q1_f5 (sonnet)

Done. 5 responses saved to study/results/raw/outputs_sonnet_<timestamp>.csv
```

- [ ] **Step 2: Read the pilot outputs**

```bash
python -c "
import csv, glob
f = sorted(glob.glob('study/results/raw/*.csv'))[-1]
rows = list(csv.DictReader(open(f)))
for row in rows:
    print('=== ', row['prompt_id'], '| framing:', row['framing_label'], '| words:', row['word_count'])
    print(row['response'][:300])
    print()
"
```

Check: Do the novice (`f2`) and expert (`f4`) framings of `q1` produce noticeably different responses? If outputs look identical across all framings, the study may return a null result — that is fine and worth documenting.

- [ ] **Step 3: Delete the pilot CSV to keep results clean**

```bash
rm study/results/raw/outputs_sonnet_*.csv
```

---

### Task 7: Full Data Collection

- [ ] **Step 1: Run the full experiment (35 prompts, sonnet)**

```bash
python study/run_experiment.py sonnet
```

Expected: 35 rows. Runtime ~3–4 minutes.

- [ ] **Step 2: Verify row count**

```bash
python -c "
import csv, glob
f = sorted(glob.glob('study/results/raw/*.csv'))[-1]
rows = list(csv.DictReader(open(f)))
print(len(rows), 'rows —', f)
"
```

Expected: `35 rows`

- [ ] **Step 3 (Optional): Run a second model for comparison**

```bash
python study/run_experiment.py opus
```

This produces a second CSV. You can code and compare both separately.

- [ ] **Step 4: Commit raw results**

```bash
git add study/results/raw/
git commit -m "data: add raw API outputs for all 35 prompts"
```

---

### Task 8: Create Coding Sheet and Score All Outputs

**Files:**
- Create: `study/results/coding_sheet.csv` (generated then filled manually)

- [ ] **Step 1: Generate the blank coding sheet**

```bash
python -c "
import csv, glob

input_file = sorted(glob.glob('study/results/raw/*.csv'))[-1]
with open(input_file) as f:
    rows = list(csv.DictReader(f))

with open('study/results/coding_sheet.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=[
        'prompt_id', 'question_id', 'framing_label', 'domain',
        'word_count', 'TD', 'CC', 'RS', 'APK', 'notes'
    ])
    writer.writeheader()
    for row in rows:
        writer.writerow({
            'prompt_id': row['prompt_id'],
            'question_id': row['question_id'],
            'framing_label': row['framing_label'],
            'domain': row['domain'],
            'word_count': row['word_count'],
            'TD': '', 'CC': '', 'RS': '', 'APK': '', 'notes': ''
        })
print('Coding sheet created: study/results/coding_sheet.csv')
"
```

- [ ] **Step 2: Open the raw CSV and coding sheet side by side**

Open `study/results/raw/outputs_sonnet_*.csv` and `study/results/coding_sheet.csv` in a spreadsheet app or text editor. For each row, read the response in the raw CSV and fill in TD, CC, RS, APK in the coding sheet using `study/rubric.md`.

Budget 3–5 minutes per response. Full coding ≈ 2–3 hours. Code all rows for the same question_id together (e.g., all 5 framings of `q1`) so differences are fresh in your mind.

- [ ] **Step 3: Commit coded sheet**

```bash
git add study/results/coding_sheet.csv
git commit -m "data: add hand-coded rubric scores for all 35 outputs"
```

---

### Task 9: Analyze Results

**Files:**
- Create: `study/analyze.py`

- [ ] **Step 1: Write the analysis script**

Write `study/analyze.py`:

```python
import csv
from collections import defaultdict


FRAMING_ORDER = ["neutral", "explicit_novice", "moderate", "expert", "professional"]


def load_coded(path):
    with open(path) as f:
        return list(csv.DictReader(f))


def mean(vals):
    vals = [float(v) for v in vals if v.strip() != ""]
    return sum(vals) / len(vals) if vals else None


def fmt(v):
    return f"{v:.2f}" if v is not None else "  n/a"


def analyze(rows):
    by_framing = defaultdict(list)
    for row in rows:
        by_framing[row["framing_label"]].append(row)

    print(f"\n{'Framing':<22} {'TD':>6} {'CC':>6} {'RS':>6} {'APK':>6} {'Words':>8}")
    print("-" * 56)
    for label in FRAMING_ORDER:
        group = by_framing.get(label, [])
        if not group:
            continue
        td = mean([r["TD"] for r in group])
        cc = mean([r["CC"] for r in group])
        rs = mean([r["RS"] for r in group])
        apk = mean([r["APK"] for r in group])
        wc = mean([r["word_count"] for r in group])
        print(f"{label:<22} {fmt(td):>6} {fmt(cc):>6} {fmt(rs):>6} {fmt(apk):>6} {fmt(wc):>8}")

    print("\n--- Spread by Domain (TD range across framings) ---")
    by_domain = defaultdict(list)
    for row in rows:
        by_domain[row["domain"]].append(row)

    for domain, group in sorted(by_domain.items()):
        td_vals = [float(r["TD"]) for r in group if r["TD"].strip()]
        if td_vals:
            spread = max(td_vals) - min(td_vals)
            print(f"  {domain:<20} TD spread: {spread:.1f}  (min {min(td_vals):.1f}, max {max(td_vals):.1f})")


if __name__ == "__main__":
    rows = load_coded("study/results/coding_sheet.csv")
    analyze(rows)
```

- [ ] **Step 2: Run the analysis**

```bash
python study/analyze.py
```

Expected: a table with mean scores per framing level and a domain spread list. Look for monotonic increase in TD and APK from `explicit_novice` → `expert`, and a decrease in CC.

- [ ] **Step 3: Commit**

```bash
git add study/analyze.py
git commit -m "feat: add analysis script — mean rubric scores by framing and domain spread"
```

---

### Task 10: Write Up Findings

**Files:**
- Create: `study/report.md`

- [ ] **Step 1: Write the report**

Write `study/report.md` using this structure (fill in bracketed sections from your analysis output):

```markdown
# Does Expertise Framing Change AI Farming Advice?

## Research Question
Does claiming expertise (or lack thereof) change the advice Claude gives on
regenerative and sustainable backyard farming?

## Method
- 7 base questions across key sustainable farming domains (soil health, fertilizer,
  pest control, cover crops, composting, water conservation, no-till)
- 5 framing levels per question: neutral, explicit novice, moderate, expert, professional
- 35 total prompts run through [MODEL NAME] at temperature 0.0
- Outputs hand-coded on 4 dimensions: Technical Depth (TD), Caveat Count (CC),
  Recommendation Specificity (RS), Assumed Prior Knowledge (APK)

## Results

### Summary Table
[Paste the table printed by analyze.py here]

### Notable Patterns
[Which dimensions showed the most variation across framings?]
[Which framings diverged most from neutral?]

### Domains with Strongest Framing Effect
[From the domain spread output: which topics saw the biggest TD range?]

### Most Divergent Response Pair
[Paste the novice vs. expert response to the same question that showed the biggest gap]

## Null Results
[If any dimension showed no meaningful variation across framings, document it here
with the data. A flat table is a valid finding.]

## Implications
[2–3 paragraphs covering:]
- What this means for users who don't know to frame their expertise
- Whether differential treatment is a safety/equity concern in domains like
  health, finance, or agriculture
- What prompt designers should take away

## Limitations
- Single model tested; results may not generalize across providers
- Manual coding introduces subjectivity; inter-rater reliability not established
- 7 questions may not be representative of all sustainable farming topics
- Temperature 0.0 reduces but does not eliminate non-determinism

## Data
Raw outputs and coded sheet available in `study/results/`.
Run `python study/analyze.py` to reproduce the summary table.
```

- [ ] **Step 2: Commit**

```bash
git add study/report.md
git commit -m "docs: add final report structure"
```

---

## Summary

| Task | Output |
|------|--------|
| 1 | Repo initialized, study design written |
| 2 | 7 base questions |
| 3 | 5 framings, 35 generated prompts |
| 4 | 4-dimension rubric |
| 5 | API runner (multi-model, pilot mode) |
| 6 | Pilot validated |
| 7 | 35 raw API responses collected |
| 8 | All 35 responses hand-coded |
| 9 | Summary table + domain spread generated |
| 10 | Write-up complete |
