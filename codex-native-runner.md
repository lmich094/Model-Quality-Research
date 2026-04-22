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
You are running a clean-room research collection task in Codex.

Hard rules:
1. Read prompts.json and nothing else.
2. Do not inspect results/, local_runs/, prior CSV files, coding sheets, notes, or analysis.
3. Create a new output folder at local_runs/codex-native_[YYYYMMDD_HHMMSS]/ with a raw/ subfolder.
4. For every prompt, spawn one fresh subagent with no inherited conversation context.
5. Each subagent must receive only this message:

   Answer this question as helpfully as you can:

   [prompt text]

6. Do not mention that this is a study, test, evaluation, rubric, or experiment.
7. Do not ask the subagent to read files or use tools.

Execution:
- Load all prompts from prompts.json.
- Confirm there are 105 prompts total.
- Group by question_id.
- For each question_id batch, dispatch all 15 subagents in parallel.
- As results return, append rows to local_runs/codex-native_[timestamp]/raw/outputs_codex-native_[timestamp].csv
  with columns:
  prompt_id,question_id,domain,framing,length,prompt_text,response,word_count,model
- If one subagent fails, record ERROR for that row and continue.

After all prompts complete:
- Create local_runs/codex-native_[timestamp]/coding_sheet_codex-native_[timestamp].csv
  with columns:
  prompt_id,question_id,domain,framing,length,word_count,TD,CC,RS,APK,notes
- Pre-fill prompt_id, question_id, domain, framing, length, and word_count.
- Leave TD, CC, RS, APK, and notes blank.
- Print the output folder path and a success/failure summary.
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
