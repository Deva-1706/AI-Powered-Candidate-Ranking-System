import json
import csv
from candidate_scorer import calculate_score

candidates = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            candidate = json.loads(line)

            score = calculate_score(candidate)

            candidates.append({
                "candidate_id": candidate["candidate_id"],
                "score": score,
                "reasoning": "Strong experience, education, and skills match."
            })

candidates.sort(
    key=lambda x: x["score"],
    reverse=True
)

with open("DEVANATH.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow([
        "candidate_id",
        "rank",
        "score",
        "reasoning"
    ])

    for rank, candidate in enumerate(candidates[:100], start=1):
        writer.writerow([
            candidate["candidate_id"],
            rank,
            candidate["score"],
            candidate["reasoning"]
        ])

print("DEVANATH.csv generated successfully")