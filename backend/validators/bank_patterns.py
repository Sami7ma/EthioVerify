import re

BANK_PATTERNS = {
    "CBE": r"^FT\d{2}[A-Z0-9]{8}$",
    "BOA": r"^BOA\d{10}$",
    "AWASH": r"^AW\d{8}$"
}


def detect_bank(text: str):
    text = text.upper()

    if "COMMERCIAL BANK OF ETHIOPIA" in text:
        return "CBE"
    if "BANK OF ABYSSINIA" in text:
        return "BOA"
    if "AWASH BANK" in text:
        return "AWASH"

    return "UNKNOWN"


def validate_transaction_id(txn_id: str, bank: str):
    if bank not in BANK_PATTERNS:
        return False

    pattern = BANK_PATTERNS[bank]
    return re.match(pattern, txn_id) is not None