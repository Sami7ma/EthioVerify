from pydantic import BaseModel
from typing import Optional

class ReceiptResponse(BaseModel):
    transaction_id: Optional[str]
    amount: Optional[str]
    date: Optional[str]
    suspicious_material: bool
    raw_text: str
