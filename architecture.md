# Swarm Architecture

This document explains how to run the study using a subagent swarm so it can be ported to any platform — Claude Code, OpenAI Codex, Gemini, or a plain Python script.

---

## Overview

The study uses a 3-tier architecture:

```
Orchestrator
├── Subagent 1 (Q1 - Soil Health)      → 15 fresh API calls → 15 responses recorded
├── Subagent 2 (Q2 - Fertilizer)       → 15 fresh API calls → 15 responses recorded
├── Subagent 3 (Q3 - Pest Control)     → 15 fresh API calls → 15 responses recorded
├── Subagent 4 (Q4 - Cover Crops)      → 15 fresh API calls → 15 responses recorded
├── Subagent 5 (Q5 - Composting)       → 15 fresh API calls → 15 responses recorded
├── Subagent 6 (Q6 - Water Conservation) → 15 fresh API calls → 15 responses recorded
└── Subagent 7 (Q7 - No-Till)          → 15 fresh API calls → 15 responses recorded
```

All 7 subagents run in parallel. Each subagent handles one question domain, making 15 sequential API calls to the target model — one per prompt — and returns all 15 results to the orchestrator.

**Total per model run:** 105 API calls to the target model, 7 subagent instances, 1 orchestrator.

---

## The Critical Invariant

**Every call to the target model must be a fresh, independent API request with no shared message history.**

This is what ensures experimental validity. The target model must never see a previous prompt or response when answering the current one. Each of the 105 API calls passes only the single prompt in the messages array — nothing else.

```
# CORRECT — fresh context every time
response = target_model.chat([{"role": "user", "content": prompt["text"]}])

# WRONG — carries contaminating history
history.append({"role": "user", "content": prompt["text"]})
response = target_model.chat(history)
```

The subagent's own context grows as it accumulates results, but that does not affect the target model — the target model only ever sees one prompt at a time.

---

## What Each Tier Knows

### Orchestrator
- Reads `prompts.json`
- Groups prompts by `question_id` (Q1–Q7)
- Dispatches 7 subagents in parallel, giving each only their 15 prompts
- Collects results and writes to `results/raw/`

### Subagent (receives from orchestrator)
- Target model name and API credentials
- Their 15 prompts (extracted from `prompts.json` — not the full file)
- Output filename to write results to
- The critical invariant above

### Target Model (receives from subagent)
- One prompt at a time
- Nothing else

---

## Subagent Instruction Template

This is the full context a subagent needs. Keep it minimal.

```
You are a data collection agent running a research study.

Target model: {MODEL_NAME}
Your domain: {DOMAIN}
Output file: results/raw/{DOMAIN}_{MODEL}_{TIMESTAMP}.csv

CRITICAL: Each prompt below must be sent as a completely fresh API call
with no shared message history. Do not pass previous prompts or responses
into subsequent calls.

For each prompt:
1. Make a new API call to {MODEL_NAME} with only that prompt as the message
2. Record: prompt_id, prompt_text, response_text, word_count
3. Append the result to {OUTPUT_FILE}

Prompts to run:
{JSON_LIST_OF_15_PROMPTS}

Return a summary: how many completed successfully, any errors.
```

---

## Platform Porting Guide

### Claude Code (native)

Use the built-in `Agent` tool. Dispatch all 7 subagents in a single message to run in parallel.

```python
# Orchestrator pseudo-code
import json

prompts = json.load(open("prompts.json"))
by_question = {}
for p in prompts["prompts"]:
    by_question.setdefault(p["question_id"], []).append(p)

# Dispatch 7 subagents simultaneously (single Agent tool call block)
for q_id, batch in by_question.items():
    Agent(
        description=f"Run {q_id} prompts against target model",
        prompt=subagent_template.format(
            domain=batch[0]["domain"],
            prompts=json.dumps(batch)
        )
    )
```

### OpenAI (Codex / Assistants API)

Use the Assistants API with parallel thread creation. Each thread = one subagent.

```python
import openai, json

client = openai.OpenAI()
prompts = json.load(open("prompts.json"))
by_question = {}
for p in prompts["prompts"]:
    by_question.setdefault(p["question_id"], []).append(p)

threads = []
for q_id, batch in by_question.items():
    thread = client.beta.threads.create()
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=subagent_template.format(
            domain=batch[0]["domain"],
            prompts=json.dumps(batch)
        )
    )
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=ASSISTANT_ID
    )
    threads.append((thread.id, run.id, q_id))

# Poll all threads until complete, collect results
```

### Gemini (Vertex AI / Google AI Studio)

Use parallel async calls. Gemini does not have a native agent-dispatch mechanism equivalent to Claude Code's `Agent` tool, so dispatch via Python async.

```python
import asyncio
import google.generativeai as genai
import json

prompts = json.load(open("prompts.json"))
by_question = {}
for p in prompts["prompts"]:
    by_question.setdefault(p["question_id"], []).append(p)

async def run_subagent(q_id, batch):
    model = genai.GenerativeModel("gemini-pro")
    instruction = subagent_template.format(
        domain=batch[0]["domain"],
        prompts=json.dumps(batch)
    )
    response = await model.generate_content_async(instruction)
    return q_id, response.text

async def main():
    tasks = [run_subagent(q, b) for q, b in by_question.items()]
    results = await asyncio.gather(*tasks)
    # write results

asyncio.run(main())
```

### Universal Fallback (plain Python, any model)

If the target platform doesn't support parallel agent dispatch, run sequentially. Slower but identical results.

```python
import json, csv, time
from datetime import datetime

def call_target_model(prompt_text, model_client):
    # Replace with the actual SDK call for your target model
    # IMPORTANT: fresh call, no history
    response = model_client.chat([
        {"role": "user", "content": prompt_text}
    ])
    return response.text

def run_study(prompts_path, model_client, model_name):
    prompts = json.load(open(prompts_path))["prompts"]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output = f"results/raw/outputs_{model_name}_{timestamp}.csv"

    with open(output, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "prompt_id", "domain", "framing", "length",
            "prompt_text", "response", "word_count", "model"
        ])
        writer.writeheader()
        for i, prompt in enumerate(prompts):
            print(f"[{i+1}/105] {prompt['id']}")
            response_text = call_target_model(prompt["text"], model_client)
            writer.writerow({
                "prompt_id": prompt["id"],
                "domain": prompt["domain"],
                "framing": prompt["framing"],
                "length": prompt["length"],
                "prompt_text": prompt["text"],
                "response": response_text,
                "word_count": len(response_text.split()),
                "model": model_name
            })
            time.sleep(0.5)  # avoid rate limits

    print(f"Done. Results saved to {output}")
```

---

## Results File Format

Each subagent writes a CSV to `results/raw/` with this schema:

| Field | Type | Description |
|-------|------|-------------|
| `prompt_id` | string | e.g. `Q1-EXP-M` |
| `domain` | string | e.g. `soil_health` |
| `framing` | string | `N`, `NOV`, `MOD`, `EXP`, or `PRO` |
| `length` | string | `S`, `M`, or `L` |
| `prompt_text` | string | Full text of the prompt sent |
| `response` | string | Full text of the model's response |
| `word_count` | integer | Word count of the response |
| `model` | string | Model name and version |

After all subagents complete, the orchestrator merges all CSVs into a single `results/raw/outputs_{model}_{timestamp}.csv`.

---

## Token Budget (per model run)

| Component | Estimated tokens |
|-----------|-----------------|
| Orchestrator context (prompts.json + dispatch + collect) | ~25,000–40,000 |
| Per subagent (instructions + 15 prompts + 15 responses accumulated) | ~10,000–18,000 |
| 7 subagents total | ~70,000–126,000 |
| **Total Claude orchestration tokens** | **~95,000–166,000** |
| Target model input (105 prompts) | ~16,000 |
| Target model output (105 responses, ~400 words each) | ~56,000 |

Well within the 1M context window. Running 3 models stays under 600K total.

---

## File Reference

| File | Purpose |
|------|---------|
| `prompts.json` | All 105 prompts in structured JSON — primary input for subagents |
| `subagent-instructions.md` | The minimal instruction template each subagent receives |
| `README.md` | Full study methodology and all prompts in human-readable format |
| `study-lite-35.md` | Simplified 35-prompt version (framing only, no length variable) |
| `results/raw/` | Raw CSV outputs per model run |
| `results/coding_sheet.csv` | Hand-coded rubric scores |
