# Subagent Instructions Template

This is the complete context a subagent receives from the orchestrator. Everything outside this template is unnecessary and should not be passed to the subagent.

---

## Template

```
You are a data collection agent for a research study.

TARGET MODEL: {MODEL_NAME}
YOUR DOMAIN: {DOMAIN}
OUTPUT FILE: results/raw/{DOMAIN}_{MODEL}_{TIMESTAMP}.csv

CRITICAL RULE: Every prompt below must be sent as a completely separate,
fresh API call. Do not pass any previous prompts or responses into
subsequent calls. Each call gets one prompt and nothing else.

TASK:
For each of the {N} prompts below, in order:
1. Send only that prompt's "text" field as a new message to {MODEL_NAME}
2. Record the full response
3. Append one row to {OUTPUT_FILE} with these fields:
   - prompt_id
   - domain
   - framing
   - length
   - prompt_text
   - response
   - word_count (count words in response)
   - model

PROMPTS:
{JSON_ARRAY_OF_15_PROMPTS}

When done, return: "Completed {N}/{N} prompts for domain {DOMAIN}. Output written to {OUTPUT_FILE}."
If any call fails, note the prompt_id and error, skip it, and continue.
```

---

## What the Orchestrator Fills In

| Placeholder | Value |
|-------------|-------|
| `{MODEL_NAME}` | e.g. `gpt-4o`, `claude-opus-4-7`, `gemini-1.5-pro` |
| `{DOMAIN}` | e.g. `soil_health`, `fertilizer`, `pest_control` |
| `{TIMESTAMP}` | ISO timestamp at run start, e.g. `20260422_143000` |
| `{N}` | Always 15 |
| `{JSON_ARRAY_OF_15_PROMPTS}` | The 15 prompts for this domain, extracted from `prompts.json` |

---

## How the Orchestrator Extracts Each Subagent's Batch

```python
import json

with open("prompts.json") as f:
    all_prompts = json.load(f)["prompts"]

by_domain = {}
for p in all_prompts:
    by_domain.setdefault(p["domain"], []).append(p)

# Each subagent gets only its 15 prompts
for domain, batch in by_domain.items():
    subagent_context = template.format(
        MODEL_NAME=target_model,
        DOMAIN=domain,
        TIMESTAMP=timestamp,
        N=len(batch),
        JSON_ARRAY_OF_15_PROMPTS=json.dumps(batch, indent=2)
    )
    # dispatch subagent with subagent_context
```

---

## What a Filled-In Subagent Instruction Looks Like

```
You are a data collection agent for a research study.

TARGET MODEL: gpt-4o
YOUR DOMAIN: soil_health
OUTPUT FILE: results/raw/soil_health_gpt-4o_20260422_143000.csv

CRITICAL RULE: Every prompt below must be sent as a completely separate,
fresh API call. Do not pass any previous prompts or responses into
subsequent calls. Each call gets one prompt and nothing else.

TASK:
For each of the 15 prompts below, in order:
1. Send only that prompt's "text" field as a new message to gpt-4o
2. Record the full response
3. Append one row to results/raw/soil_health_gpt-4o_20260422_143000.csv with these fields:
   - prompt_id
   - domain
   - framing
   - length
   - prompt_text
   - response
   - word_count (count words in response)
   - model

PROMPTS:
[
  {
    "id": "Q1-N-S",
    "question_id": "Q1",
    "domain": "soil_health",
    "framing": "N",
    "length": "S",
    "text": "What's the best way to improve soil health in my backyard garden?"
  },
  {
    "id": "Q1-N-M",
    ...
  },
  ... (15 total)
]

When done, return: "Completed 15/15 prompts for domain soil_health. Output written to results/raw/soil_health_gpt-4o_20260422_143000.csv."
If any call fails, note the prompt_id and error, skip it, and continue.
```

---

## Token Cost Per Subagent

| Component | Tokens |
|-----------|--------|
| Fixed instruction text | ~300 |
| 15 prompts (JSON) | ~2,500 |
| Accumulated responses (15 × ~400 words) | ~8,500 |
| **Total per subagent** | **~11,300** |

Across 7 subagents: ~79,000 tokens. The orchestrator adds ~25,000–40,000. Total well under 200,000 tokens per model run.
