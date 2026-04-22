#!/usr/bin/env python3
"""
AI Framing Study — Analysis Script

Reads a completed coding sheet and outputs summary statistics.

Usage:
    python analyze.py --scores results/coding_sheet_claude_20260422.csv
    python analyze.py --scores results/coding_sheet_claude_20260422.csv --compare results/coding_sheet_gpt_20260422.csv
"""

import argparse
import csv
from collections import defaultdict


FRAMING_ORDER = ["N", "NOV", "MOD", "EXP", "PRO"]
FRAMING_LABELS = {
    "N": "Neutral",
    "NOV": "Novice",
    "MOD": "Moderate",
    "EXP": "Expert",
    "PRO": "Professional",
}
LENGTH_ORDER = ["S", "M", "L"]
LENGTH_LABELS = {"S": "Short", "M": "Medium", "L": "Long"}
DIMENSIONS = ["TD", "CC", "RS", "APK"]


def load_scores(path):
    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    # Filter to rows that have at least one score filled in
    scored = [r for r in rows if any(r.get(d, "").strip() for d in DIMENSIONS)]
    if not scored:
        print(f"Warning: no scored rows found in {path}")
    return scored


def mean(vals):
    vals = [float(v) for v in vals if str(v).strip() not in ("", "n/a", "N/A")]
    return round(sum(vals) / len(vals), 2) if vals else None


def fmt(v, width=6):
    return f"{v:{width}.2f}" if v is not None else f"{'n/a':>{width}}"


def print_table(title, groups, order, labels, rows):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")
    header = f"{'Group':<22}" + "".join(f"{d:>7}" for d in DIMENSIONS) + f"{'Words':>8}"
    print(header)
    print("-" * len(header))
    for key in order:
        group = groups.get(key, [])
        if not group:
            continue
        label = labels.get(key, key)
        td = mean([r["TD"] for r in group])
        cc = mean([r["CC"] for r in group])
        rs = mean([r["RS"] for r in group])
        apk = mean([r["APK"] for r in group])
        wc = mean([r["word_count"] for r in group])
        print(f"{label:<22}" + fmt(td) + fmt(cc) + fmt(rs) + fmt(apk) + fmt(wc, 8))


def analyze(path, label=None):
    rows = load_scores(path)
    tag = label or path
    n = len(rows)

    print(f"\n{'#'*60}")
    print(f"  Results: {tag}  ({n} scored responses)")
    print(f"{'#'*60}")

    # --- By framing ---
    by_framing = defaultdict(list)
    for r in rows:
        by_framing[r["framing"]].append(r)
    print_table("By Framing Level", by_framing, FRAMING_ORDER, FRAMING_LABELS, rows)

    # --- By length ---
    by_length = defaultdict(list)
    for r in rows:
        by_length[r["length"]].append(r)
    print_table("By Prompt Length", by_length, LENGTH_ORDER, LENGTH_LABELS, rows)

    # --- Framing x Length interaction ---
    print(f"\n{'='*60}")
    print("  Framing × Length Interaction (TD only)")
    print(f"{'='*60}")
    header = f"{'Framing':<16}" + "".join(f"{LENGTH_LABELS[l]:>10}" for l in LENGTH_ORDER)
    print(header)
    print("-" * len(header))
    for f_key in FRAMING_ORDER:
        row_str = f"{FRAMING_LABELS.get(f_key, f_key):<16}"
        for l_key in LENGTH_ORDER:
            group = [r for r in rows if r["framing"] == f_key and r["length"] == l_key]
            td = mean([r["TD"] for r in group])
            row_str += fmt(td, 10)
        print(row_str)

    # --- By domain (TD spread) ---
    print(f"\n{'='*60}")
    print("  TD Spread by Domain (max framing effect per topic)")
    print(f"{'='*60}")
    by_domain = defaultdict(list)
    for r in rows:
        by_domain[r["domain"]].append(r)

    domain_spreads = []
    for domain, group in sorted(by_domain.items()):
        td_vals = [float(r["TD"]) for r in group if r.get("TD", "").strip()]
        if td_vals:
            spread = max(td_vals) - min(td_vals)
            domain_spreads.append((spread, domain, min(td_vals), max(td_vals)))

    domain_spreads.sort(reverse=True)
    for spread, domain, mn, mx in domain_spreads:
        bar = "█" * int(spread * 4)
        print(f"  {domain:<22} spread={spread:.1f}  ({mn:.1f}–{mx:.1f})  {bar}")

    # --- Biggest individual divergence ---
    print(f"\n{'='*60}")
    print("  Most Divergent Prompt Pairs (same question, NOV vs EXP)")
    print(f"{'='*60}")
    by_question = defaultdict(dict)
    for r in rows:
        by_question[r["question_id"]][r["framing"]] = r

    pairs = []
    for q_id, framings in by_question.items():
        nov = framings.get("NOV")
        exp = framings.get("EXP")
        if nov and exp:
            for dim in DIMENSIONS:
                try:
                    diff = abs(float(exp[dim]) - float(nov[dim]))
                    pairs.append((diff, dim, q_id, nov[dim], exp[dim]))
                except (ValueError, KeyError):
                    pass

    pairs.sort(reverse=True)
    seen = set()
    for diff, dim, q_id, nov_val, exp_val in pairs[:10]:
        key = (q_id, dim)
        if key not in seen:
            seen.add(key)
            print(f"  {q_id} | {dim}: NOV={nov_val} → EXP={exp_val} (Δ={diff:.1f})")


def compare(path_a, path_b, label_a, label_b):
    rows_a = load_scores(path_a)
    rows_b = load_scores(path_b)

    print(f"\n{'#'*60}")
    print(f"  Model Comparison: {label_a} vs {label_b}")
    print(f"{'#'*60}")

    for framing in FRAMING_ORDER:
        group_a = [r for r in rows_a if r["framing"] == framing]
        group_b = [r for r in rows_b if r["framing"] == framing]
        label = FRAMING_LABELS.get(framing, framing)
        print(f"\n  {label}:")
        for dim in DIMENSIONS:
            a_val = mean([r[dim] for r in group_a])
            b_val = mean([r[dim] for r in group_b])
            diff = round(b_val - a_val, 2) if a_val is not None and b_val is not None else None
            diff_str = f"  Δ={diff:+.2f}" if diff is not None else ""
            print(f"    {dim}: {label_a}={fmt(a_val).strip()}  {label_b}={fmt(b_val).strip()}{diff_str}")


def main():
    parser = argparse.ArgumentParser(description="Analyze scored rubric results.")
    parser.add_argument("--scores", required=True, help="Path to completed coding sheet CSV.")
    parser.add_argument("--label", default=None, help="Label for this model (e.g. 'Claude Sonnet').")
    parser.add_argument("--compare", default=None, help="Path to a second coding sheet to compare against.")
    parser.add_argument("--compare-label", default=None, help="Label for the comparison model.")
    args = parser.parse_args()

    analyze(args.scores, args.label)

    if args.compare:
        compare(
            args.scores, args.compare,
            args.label or args.scores,
            args.compare_label or args.compare,
        )


if __name__ == "__main__":
    main()
