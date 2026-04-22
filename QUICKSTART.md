# Quickstart

This guide takes you from a fresh clone to a fully analyzed set of results.

---

## What This Repo Does

Runs 105 farming advice prompts through an AI model, varies two things — how the user frames their expertise and how much context they provide — and measures whether those variables change the quality of the model's response.

Full methodology: `README.md`
Architecture and porting guide: `architecture.md`
Scoring rubric with calibration examples: `rubric.md`

---

## Prerequisites

- Python 3.9+
- An Anthropic API key and/or OpenAI API key
- ~$1–5 per full model run (105 API calls)

---

## Setup

```bash
# 1. Clone
git clone https://github.com/lmich094/Model-Quality-Research.git
cd Model-Quality-Research

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up API keys
cp .env.example .env
# Open .env and replace the placeholder values with your real keys
```

---

## Step 1 — Pilot Run (5 prompts, verify everything works)

```bash
python runner.py --model claude --limit 5
```

Check that `results/raw/outputs_claude_*.csv` was created and has 5 rows with real responses. If it fails, check that `ANTHROPIC_API_KEY` is set correctly in `.env`.

For GPT instead:
```bash
python runner.py --model gpt --limit 5
```

---

## Step 2 — Full Run (105 prompts)

```bash
python runner.py --model claude
```

Runtime: ~5–8 minutes. Output:
- `results/raw/outputs_claude_[timestamp].csv` — all 105 responses
- `results/coding_sheet_claude_[timestamp].csv` — blank scoring sheet

To test a second model:
```bash
python runner.py --model gpt
```

---

## Step 3 — Score the Responses

Open `results/raw/outputs_claude_[timestamp].csv` and `results/coding_sheet_claude_[timestamp].csv` side by side.

For each row, read the response in the raw file and fill in the four scores in the coding sheet:
- **TD** (1–5): Technical depth of vocabulary
- **CC** (count): Number of hedging/warning sentences
- **RS** (1–3): Specificity of recommendations
- **APK** (1–3): How much prior knowledge the response assumes

**Read `rubric.md` before you start.** It has worked calibration examples with reasoning. Budget 3–5 minutes per response, ~2–3 hours total for 105 responses.

Alternatively, pass the raw responses to an AI model with `rubric.md` as context and ask it to score each one — see `rubric.md` for the dimension descriptions to include in that prompt.

---

## Step 4 — Analyze

```bash
python analyze.py --scores results/coding_sheet_claude_[timestamp].csv --label "Claude Sonnet"
```

Outputs:
- Mean scores by framing level (N → NOV → MOD → EXP → PRO)
- Mean scores by prompt length (S → M → L)
- Framing × Length interaction table (TD only)
- Domain spread (which topics showed the biggest framing effect)
- Most divergent NOV vs EXP pairs

To compare two models:
```bash
python analyze.py \
  --scores results/coding_sheet_claude_[timestamp].csv --label "Claude" \
  --compare results/coding_sheet_gpt_[timestamp].csv --compare-label "GPT-4o"
```

---

## Supported Models

| Flag | Model |
|------|-------|
| `--model claude` | Claude Sonnet 4.6 |
| `--model claude-opus` | Claude Opus 4.7 |
| `--model gpt` | GPT-4o |
| `--model gpt-mini` | GPT-4o Mini |

To add a new model, add an entry to the `MODELS` dict in `runner.py` and implement a call function if the provider isn't already supported.

---

## Run a Single Domain (15 prompts)

```bash
python runner.py --model claude --domain soil_health
```

Valid domain values: `soil_health`, `fertilizer`, `pest_control`, `cover_crops`, `composting`, `water_conservation`, `no_till`

---

## File Reference

| File | Purpose |
|------|---------|
| `prompts.json` | All 105 prompts as structured JSON — do not edit |
| `runner.py` | Runs prompts against a model, outputs raw CSV + blank coding sheet |
| `analyze.py` | Reads completed coding sheet, outputs summary tables |
| `rubric.md` | Scoring rubric with calibration examples — read before scoring |
| `requirements.txt` | Python dependencies |
| `.env.example` | API key template |
| `README.md` | Full study methodology and all prompts in human-readable form |
| `study-lite-35.md` | 35-prompt version (framing only, no length variable) |
| `architecture.md` | Swarm design and porting guide for other platforms |
| `subagent-instructions.md` | Minimal subagent instruction template |
| `results/raw/` | Raw API responses (created on first run) |
| `results/coding_sheet_*.csv` | Scoring sheets (created by runner, filled in by you) |
