#!/usr/bin/env python3
"""
AI Framing Study — Experiment Runner

Runs all 105 prompts (or a subset) against a target model.
Each prompt is sent as a fresh, independent API call with no shared history.

Usage:
    python runner.py --model claude          # Run all 105 prompts against Claude Sonnet
    python runner.py --model gpt            # Run all 105 prompts against GPT-4o
    python runner.py --model claude --limit 5           # Pilot: first 5 prompts only
    python runner.py --model gpt --domain soil_health   # One domain only (15 prompts)

Supported models: claude, claude-opus, gpt, gpt-mini
"""

import argparse
import csv
import json
import os
import time
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# --- Model registry ---
MODELS = {
    "claude": {
        "provider": "anthropic",
        "model_id": "claude-sonnet-4-6",
        "display": "Claude Sonnet 4.6",
    },
    "claude-opus": {
        "provider": "anthropic",
        "model_id": "claude-opus-4-7",
        "display": "Claude Opus 4.7",
    },
    "gpt": {
        "provider": "openai",
        "model_id": "gpt-4o",
        "display": "GPT-4o",
    },
    "gpt-mini": {
        "provider": "openai",
        "model_id": "gpt-4o-mini",
        "display": "GPT-4o Mini",
    },
}

TEMPERATURE = 0.0
MAX_TOKENS = 1024


# --- Provider call functions ---
# Each function makes ONE fresh API call and returns the response text.
# No history is ever passed between calls.

def call_anthropic(prompt_text, model_id):
    import anthropic
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    response = client.messages.create(
        model=model_id,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        messages=[{"role": "user", "content": prompt_text}],
    )
    return response.content[0].text


def call_openai(prompt_text, model_id):
    from openai import OpenAI
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.chat.completions.create(
        model=model_id,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        messages=[{"role": "user", "content": prompt_text}],
    )
    return response.choices[0].message.content


PROVIDERS = {
    "anthropic": call_anthropic,
    "openai": call_openai,
}


def call_model(prompt_text, model_key):
    config = MODELS[model_key]
    fn = PROVIDERS[config["provider"]]
    return fn(prompt_text, config["model_id"])


# --- Coding sheet generator ---
# Creates a blank CSV the human fills in with rubric scores after reviewing responses.

def generate_coding_sheet(prompts, model_key, timestamp):
    path = f"results/coding_sheet_{model_key}_{timestamp}.csv"
    fieldnames = [
        "prompt_id", "question_id", "domain", "framing", "length",
        "word_count", "TD", "CC", "RS", "APK", "notes",
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for p in prompts:
            writer.writerow({
                "prompt_id": p["id"],
                "question_id": p["question_id"],
                "domain": p["domain"],
                "framing": p["framing"],
                "length": p["length"],
                "word_count": p.get("word_count", ""),
                "TD": "", "CC": "", "RS": "", "APK": "", "notes": "",
            })
    return path


# --- Main ---

def main():
    parser = argparse.ArgumentParser(
        description="Run AI framing study prompts against a target model."
    )
    parser.add_argument(
        "--model", required=True, choices=list(MODELS.keys()),
        help="Which model to test.",
    )
    parser.add_argument(
        "--limit", type=int, default=None,
        help="Stop after this many prompts. Use for pilot runs.",
    )
    parser.add_argument(
        "--domain", default=None,
        help="Run only prompts for one domain (e.g. soil_health, fertilizer).",
    )
    args = parser.parse_args()

    # Load prompts
    with open("prompts.json") as f:
        all_prompts = json.load(f)["prompts"]

    prompts = all_prompts
    if args.domain:
        prompts = [p for p in prompts if p["domain"] == args.domain]
        if not prompts:
            valid = sorted({p["domain"] for p in all_prompts})
            print(f"Unknown domain '{args.domain}'. Valid options: {valid}")
            return
    if args.limit:
        prompts = prompts[: args.limit]

    # Setup output paths
    Path("results/raw").mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    raw_path = f"results/raw/outputs_{args.model}_{timestamp}.csv"

    config = MODELS[args.model]
    print(f"\nRunning {len(prompts)} prompts against {config['display']}")
    print(f"Output: {raw_path}\n")

    raw_fieldnames = [
        "prompt_id", "question_id", "domain", "framing", "length",
        "prompt_text", "response", "word_count", "model", "model_id", "timestamp",
    ]

    completed = []
    errors = []

    with open(raw_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=raw_fieldnames)
        writer.writeheader()

        for i, prompt in enumerate(prompts):
            print(f"[{i+1}/{len(prompts)}] {prompt['id']}...", end=" ", flush=True)

            try:
                response_text = call_model(prompt["text"], args.model)
                word_count = len(response_text.split())
                print(f"{word_count} words")
                status = "ok"
            except Exception as e:
                response_text = f"ERROR: {e}"
                word_count = 0
                print(f"FAILED — {e}")
                errors.append(prompt["id"])
                status = "error"

            prompt["word_count"] = word_count  # attach for coding sheet

            writer.writerow({
                "prompt_id": prompt["id"],
                "question_id": prompt["question_id"],
                "domain": prompt["domain"],
                "framing": prompt["framing"],
                "length": prompt["length"],
                "prompt_text": prompt["text"],
                "response": response_text,
                "word_count": word_count,
                "model": args.model,
                "model_id": config["model_id"],
                "timestamp": datetime.now().isoformat(),
            })

            completed.append(prompt["id"])
            time.sleep(0.5)  # rate limit buffer

    # Generate blank coding sheet
    coding_path = generate_coding_sheet(prompts, args.model, timestamp)

    # Summary
    print(f"\n{'='*50}")
    print(f"Done. {len(completed) - len(errors)}/{len(prompts)} succeeded.")
    if errors:
        print(f"Failed prompt IDs: {errors}")
    print(f"\nRaw responses: {raw_path}")
    print(f"Blank coding sheet: {coding_path}")
    print(f"\nNext step: open both files side by side.")
    print(f"Read each response in {raw_path}, score it in {coding_path} using rubric.md.")
    print(f"Then run: python analyze.py --scores {coding_path}")


if __name__ == "__main__":
    main()
