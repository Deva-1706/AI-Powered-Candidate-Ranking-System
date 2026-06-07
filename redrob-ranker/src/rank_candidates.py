import json
from candidate_scorer import calculate_score

candidates = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            candidate = json.loads(line)
            score = calculate_score(candidate)

            candidates.append({
                "candidate_id": candidate["candidate_id"],
                "score": score
            })

candidates.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("Top 10 Candidates")

for candidate in candidates[:10]:
    print(candidate)