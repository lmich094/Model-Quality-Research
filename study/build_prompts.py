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
