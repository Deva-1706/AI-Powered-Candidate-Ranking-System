import json

def load_candidates(file_path):
    candidates = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                candidates.append(json.loads(line))

    return candidates

candidates = load_candidates("data/candidates.jsonl")

print("Total Candidates:", len(candidates))