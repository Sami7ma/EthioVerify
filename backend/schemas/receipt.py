from pydantic import BaseModel
from typing import Optional

class ReceiptResponse(BaseModel):
    transaction_id: str
    amount: str
    date: str
    suspicious_metadata: bool
    raw_text: str
    ela_heatmap_path: str

    #phase 3
    bank_detected: str
    risk_flags: list[str]
    rule_score: float

    #phase 4
    final_score: float
    classification: str
    