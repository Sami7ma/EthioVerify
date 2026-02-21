# Ethio-Verify 🔐

Ethio-Verify is a forensic verification system designed to detect tampered Ethiopian bank payment screenshots using OCR, metadata analysis, and digital image forensics.

This project demonstrates backend engineering, image processing, and fraud detection techniques.

---

## 🚀 Features (Phase 1)

- 📸 Image upload via FastAPI
- 🔍 EXIF metadata extraction
- ⚠ Detection of suspicious editing software (Adobe, Canva, etc.)
- 🧠 OCR-based text extraction (Transaction ID, Amount, Date)
- 🧾 Regex validation of extracted fields
- 📊 Structured JSON response

---

## 🧱 Tech Stack

| Layer | Technology | Purpose |
|--------|------------|----------|
| Backend | FastAPI | API framework |
| OCR | EasyOCR | Text extraction |
| Image Processing | Pillow | Metadata & image handling |
| Forensics (Next Phase) | OpenCV | Error Level Analysis |
| Database (Phase 3) | PostgreSQL | Transaction verification |

---

## 📁 Project Structure

```
/receipt-verifier
├── /backend
│   ├── /api
│   ├── /forensics
│   ├── /ocr
│   ├── /schemas
│   └── main.py
└── requirements.txt
```

---

## ⚙ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ethio-verify.git
cd receipt-verifier/backend
```

### 2️⃣ Install Dependencies

```bash
pip install fastapi uvicorn pillow easyocr python-multipart
pip install opencv-python numpy
```

### 3️⃣ Run Server

```bash
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 📦 Sample API Response

```json
{
  "transaction_id": "TXN-12345-ABC",
  "amount": "1500.00",
  "date": "2026-02-18",
  "suspicious_metadata": false,
  "raw_text": "..."
}
```

---
## 📊 Architecture Diagram
User Upload
     ↓
FastAPI Endpoint
     ↓
Metadata Check (Pillow)
     ↓
OCR Extraction (EasyOCR)
     ↓
Regex Validation
     ↓
Structured JSON Response

## 🔬 Roadmap

### Phase 2
- Error Level Analysis (ELA)
- Blur & texture detection using OpenCV
- Heatmap generation

### Phase 3
- PostgreSQL transaction database
- Source-of-truth verification
- Logical fraud checks

### Phase 4
- Fraud scoring engine
- Next.js security dashboard
- Visual forensic heatmaps

---

## 🎯 Purpose

This project is built as a portfolio demonstration of:

- Backend system architecture
- Digital image forensics
- OCR integration
- Fraud detection logic
- Clean API design

---

## 👨‍💻 Author

Samuel  
Software Engineering Student  
Focused on Backend Systems, Computer Vision & Secure Application Design.
