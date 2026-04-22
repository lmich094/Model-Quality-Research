# Codex-Native Runner

This workflow is the Codex-native path for collecting responses with fresh subagents.
It is designed to keep the run clean:

- Read `prompts.json` and nothing else.
- Do not open any existing files under `results/` or `local_runs/`.
- Write all new artifacts to a brand-new timestamped folder under `local_runs/`.
- Give each subagent exactly one prompt and no experiment context.

## Important Constraint

This document describes a Codex-native workflow, not an API workflow.
Responses collected through this path come from the Codex host model in this environment.

## Clean-Room Rules

1. Start in a workspace where any prior output files have been deleted or ignored.
2. Read only `prompts.json`.
3. Do not read `results/`, `local_runs/`, prior CSVs, coding sheets, notes, or analyses.
4. Dispatch one fresh subagent per prompt with no forked conversation context.
5. Each subagent should answer directly and should not use tools or inspect files.
6. The orchestrator may write CSV files locally after each response returns.

## Output Location

Create a fresh folder for each run:

```text
local_runs/codex-native_[YYYYMMDD_HHMMSS]/
```

Write:

- `local_runs/codex-native_[timestamp]/raw/outputs_codex-native_[timestamp].csv`
- `local_runs/codex-native_[timestamp]/coding_sheet_codex-native_[timestamp].csv`

## Orchestrator Prompt

Paste the following into a fresh Codex session if you want the host tool to run the collection:

```text
You are running a research data collection task. Your job is to get Codex's
response to 105 farming questions by dispatching one fresh subagent per prompt.

Each subagent must receive ONLY the prompt text — no study context, no mention
of this being a test, no rubric. A subagent that knows it is being evaluated
may respond differently. Keep it clean.

SETUP:

Read prompts.json
Confirm you have 105 prompts
Create the output file: results/raw/outputs_codex-native_[YYYYMMDD_HHMMSS].csv
with these headers:
prompt_id, question_id, domain, framing, length, prompt_text, response, word_count, model
BATCHING RULE:
Group prompts by question_id. Run one batch per question domain.
Within each batch, dispatch the 15 subagents in three parallel waves of 6, 6, and 3 fresh subagents.
Wait for all 6 in the first wave to return before starting the second wave.
Wait for all 6 in the second wave to return before starting the third wave.
Wait for all 3 in the third wave to return before starting the next batch.
After each batch completes, append the 15 results to the CSV immediately.

SUBAGENT INSTRUCTION TEMPLATE (use exactly this — nothing more):
"Answer this question as helpfully as you can: [prompt text]"

After all 7 batches complete:

Print a summary: how many succeeded, any failures
Generate the blank coding sheet at results/coding_sheet_codex-native_[timestamp].csv
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

## Recommended Subagent Message

Use this exact format for each spawned subagent:

```text
Answer this question as helpfully as you can:

[prompt text]
```

That keeps the prompt organic while still making the task explicit.

## Notes

- One prompt per subagent is the key contamination control.
- Parallelize within each `question_id` batch only if your host agent supports it.
- This path preserves the experiment architecture while making Codex the answering model.
