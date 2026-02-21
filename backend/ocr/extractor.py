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

        transaction_id = extract_transaction_id(full_text)
        amount = extract_amount(full_text)
        date = extract_date(full_text)

        return {
            "raw_text": full_text,
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
    pattern = r"[A-Z0-9]{12,}"
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_amount(text: str):
    pattern = r"ETB\s?[\d,]+\.\d{2}"
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_date(text: str):
    pattern = r"\d{2}-[A-Za-z]{3}-\d{4}"
    match = re.search(pattern, text)
    return match.group() if match else None
