# Claude Code Native Runner

Run all 105 prompts through Claude without any API keys by using Claude Code's built-in Agent tool. Each prompt gets its own fresh subagent with zero prior context, which is the only way to guarantee experimental integrity.

---

## How It Works

```
Orchestrator (you, in a Claude Code session)
│
├── Batch 1: dispatch 15 subagents simultaneously (Q1 — Soil Health)
│   ├── SA-1  receives only: Q1-N-S   → answers → returns response
│   ├── SA-2  receives only: Q1-N-M   → answers → returns response
│   ├── ...
│   └── SA-15 receives only: Q1-PRO-L → answers → returns response
│
├── Batch 2: dispatch 15 subagents simultaneously (Q2 — Fertilizer)
│   └── ...
│
└── ... (7 batches total, 105 subagents, 105 fresh context windows)
```

**Why 1 subagent per prompt:** If a subagent answers multiple prompts sequentially, its own growing context contaminates later answers — the same problem as not starting a fresh conversation. Each subagent must receive exactly one prompt and nothing else.

---

## Instructions for the Orchestrator Session

Paste these instructions into a new Claude Code session to run the experiment.

---

### START OF ORCHESTRATOR PROMPT

```
You are running a research data collection task. Your job is to get Claude's
response to 105 farming questions by dispatching one fresh subagent per prompt.

Each subagent must receive ONLY the prompt text — no study context, no mention
of this being a test, no rubric. A subagent that knows it is being evaluated
may respond differently. Keep it clean.

SETUP:
1. Read prompts.json
2. Confirm you have 105 prompts
3. Create the output file: results/raw/outputs_claude-native_[YYYYMMDD_HHMMSS].csv
   with these headers:
   prompt_id, question_id, domain, framing, length, prompt_text, response, word_count, model

BATCHING RULE:
Group prompts by question_id. Run one batch per question domain.
Within each batch, dispatch ALL 15 subagents in a single message (parallel).
Wait for all 15 to return before starting the next batch.
After each batch completes, append the 15 results to the CSV immediately.

SUBAGENT INSTRUCTION TEMPLATE (use exactly this — nothing more):
  "Answer this question as helpfully as you can: [prompt text]"

After all 7 batches complete:
- Print a summary: how many succeeded, any failures
- Generate the blank coding sheet at results/coding_sheet_claude-native_[timestamp].csv
  with these columns pre-filled: prompt_id, question_id, domain, framing, length, word_count
  and these columns empty: TD, CC, RS, APK, notes

Batch order:
  Batch 1: all prompts where question_id = "Q1" (15 prompts)
  Batch 2: all prompts where question_id = "Q2" (15 prompts)
  Batch 3: all prompts where question_id = "Q3" (15 prompts)
  Batch 4: all prompts where question_id = "Q4" (15 prompts)
  Batch 5: all prompts where question_id = "Q5" (15 prompts)
  Batch 6: all prompts where question_id = "Q6" (15 prompts)
  Batch 7: all prompts where question_id = "Q7" (15 prompts)

If a subagent fails or returns an error, record "ERROR" in the response column,
note the prompt_id, and continue. Do not retry — move on and flag it at the end.

Begin now.
```

### END OF ORCHESTRATOR PROMPT

---

## Important Notes

**On response quality:** Claude Code subagents run under a Claude Code system prompt, which differs slightly from Claude.ai's default interface. The underlying model is the same, but responses may be slightly more structured or task-oriented. Note this when writing up results.

**On cost:** Each subagent is a Claude API call. 105 subagents = 105 API calls, consumed from whatever Claude Code plan you are on. At roughly 150 tokens in and 400 tokens out per prompt, this is approximately 58,500 tokens total — a small run.

**On parallelism:** Claude Code dispatches all Agent calls made in a single message simultaneously. The orchestrator should dispatch all 15 in one message block per batch, not one at a time. If it dispatches them sequentially, correct it: "Please dispatch all 15 subagents for this batch in a single message so they run in parallel."

**On the coding sheet:** After the run, open `results/raw/outputs_claude-native_*.csv` and `results/coding_sheet_claude-native_*.csv` side by side. Score responses using `rubric.md`. Then run `python analyze.py --scores results/coding_sheet_claude-native_*.csv`.

---

## For Other Models (Manual)

For GPT, Gemini, or any model without an API key, use `study-lite-35.md`. Every prompt is in a clean blockquote — copy one, open a fresh browser conversation, paste, copy the response into your coding sheet. Repeat 35 times per model.

35 prompts at ~2 minutes each = ~70 minutes per model.

---

## Recommended Run Order

1. **Claude** — run via this orchestrator (~10 minutes, automated)
2. **Gemini** — manual via gemini.google.com (~70 minutes, 35 prompts)
3. **ChatGPT** — manual via chatgpt.com (~70 minutes, 35 prompts)

Then compare Claude's 105-prompt results against the 35-prompt manual results for the others. Note the scope difference when writing up — Claude has full framing × length data, others have framing only.
