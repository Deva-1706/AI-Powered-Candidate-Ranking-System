from feature_engineering import (
    experience_score,
    education_score,
    skill_score
)


def calculate_score(candidate):
    exp_score = experience_score(
        candidate["profile"]["years_of_experience"]
    )

    edu_score = education_score(
        candidate["education"][0]["tier"]
        if candidate["education"]
        else "unknown"
    )

    skl_score = skill_score(
        candidate["skills"]
    )

    final_score = (
        exp_score * 0.4 +
        edu_score * 0.2 +
        skl_score * 0.4
    )

    return round(final_score, 2)