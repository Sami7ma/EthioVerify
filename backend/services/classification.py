def classify_verification(trust_score: int) -> str:
    if trust_score >= 75:
        return "Likely Authentic"
    if trust_score >= 45:
        return "Needs Manual Review"
    return "Likely Tampered"
