import easyocr
import re

# Make reader global to avoid reloading every time
try:
    reader = easyocr.Reader(['en'], gpu=False)
except Exception as e:
    print("ERROR: EasyOCR reader failed to load:", e)
    reader = None

def extract_text(image_path: str) -> dict:
    if reader is None:
        return {
            "raw_text": "",
            "transaction_id": None,
            "amount": None,
            "date": None
        }

    try:
        results = reader.readtext(image_path)
        full_text = " ".join([text[1] for text in results])
        normalized_text = " ".join(full_text.split())

        transaction_id = extract_transaction_id(normalized_text)
        amount = extract_amount(normalized_text)
        date = extract_date(normalized_text)

        return {
            "raw_text": normalized_text,
            "transaction_id": transaction_id,
            "amount": amount,
            "date": date
        }

    except Exception as e:
        print("ERROR in OCR:", e)
        return {
            "raw_text": "",
            "transaction_id": None,
            "amount": None,
            "date": None
        }

# Regex helpers
def extract_transaction_id(text: str):
    labelled_pattern = re.search(
        r"(?i)(?:transaction|trx|tx|reference|ref)\s*(?:id|no)?\s*[:\-]?\s*([A-Z0-9\-]{8,30})",
        text,
    )
    if labelled_pattern:
        return labelled_pattern.group(1)

    prefixed_pattern = re.search(r"\b(?:TXN|TRX|REF|FT)[A-Z0-9\-]{6,28}\b", text, re.IGNORECASE)
    if prefixed_pattern:
        return prefixed_pattern.group()

    generic_pattern = re.search(r"\b[A-Z0-9]{12,30}\b", text)
    return generic_pattern.group() if generic_pattern else None

def extract_amount(text: str):
    labelled_pattern = re.search(
        r"(?i)(?:amount|total|paid)\s*[:\-]?\s*(?:ETB|Birr|Br)?\s*([\d,]+(?:\.\d{2})?)",
        text,
    )
    if labelled_pattern:
        return labelled_pattern.group(1)

    currency_pattern = re.search(r"(?i)\b(?:ETB|Birr|Br)\s*([\d,]+(?:\.\d{2})?)", text)
    return currency_pattern.group(1) if currency_pattern else None

def extract_date(text: str):
    patterns = [
        r"\b\d{2}-[A-Za-z]{3}-\d{4}\b",
        r"\b\d{2}/\d{2}/\d{4}\b",
        r"\b\d{4}-\d{2}-\d{2}\b",
        r"\b\d{2}-\d{2}-\d{4}\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group()
    return None
