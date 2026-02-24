from core.config import settings

def compute_fraud_score(metadata_flag: bool,
                        ela_score: float,
                        ocr_confidence: float,
                        rule_score: float):
    
    metadata_score = 0 if metadata_flag else 100

    final_score = (
        metadata_score * settings.METADATA_WEIGHT +
        ela_score * settings.ELA_WEIGHT +
        ocr_confidence * settings.OCR_WEIGHT +
        rule_score * settings.RULE_WEIGHT
    )
    return round(final_score, 2)

def classify_score(score):
    if score <= 40:
        return "Tampered"
    elif score <= 70:
        return "Suspicious"
    else:
        return "Verified"