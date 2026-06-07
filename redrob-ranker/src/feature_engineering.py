def experience_score(years):
    if years >= 10:
        return 100
    elif years >= 6:
        return 80
    elif years >= 3:
        return 50
    else:
        return 20


def education_score(tier):
    scores = {
        "tier_1": 100,
        "tier_2": 80,
        "tier_3": 60,
        "tier_4": 40,
        "unknown": 20
    }
    return scores.get(tier, 20)


def skill_score(skills):
    score = 0

    important_skills = [
        "Python",
        "NLP",
        "Fine-tuning LLMs",
        "PyTorch",
        "TensorFlow",
        "LangChain",
        "Milvus",
        "AWS",
        "GCP"
    ]

    for skill in skills:
        if skill["name"] in important_skills:
            score += 10

    return min(score, 100)