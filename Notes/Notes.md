### 🚀 PHASE 0 — SYSTEM DESIGN FIRST

Before writing code, I must understand what I'm building. 

Today I design:

- What the system actually does

- How data flows

- What components exist

- What my GitHub will look like

## 🧠 1️⃣ CLEAR SYSTEM DEFINITION
# Project Name: 
**EthioVerify** 
**One-Line Description**
AI-Powered System that verifies Ethiopian bank payment screenshots and detects fraud.

**Who would use it?**
- small businesses
- Online sellers
- Admin reviewers

**What does user do?**
1. Register
2. Login
3. Upload Sccreenshot
4. Get verification
5. View past uploads

**What does admin do?**
1. View flagged transaction
2. Review fraud scores
3. Override status if needed

## 🏗 2️⃣ SYSTEM ARCHITECTURE (High-Level)
```
Frontend (Next.js)
        ↓
Backend API (Express)
        ↓
Upload Processing Pipeline
        ↓
OCR Engine
        ↓
Fraud Detection Engine
        ↓
PostgreSQL Database
```

## 🧩 3️⃣ CORE BACKEND MODULES
Inside the backend we will have:
```
src/
 ├── controllers/
 ├── services/
 ├── routes/
 ├── middlewares/
 ├── utils/
 ├── config/
 └── prisma/
```
***Why this structure ***
Cuz:
- Controllers = handle requests
- Services = Business logic
- Routes = Define endpoints
- MiddleWare = Auth, validation
- Utils = ocr helpers. Scoring logic
- config = Enviroment setup

## 🗄 4️⃣ DATABASE DESIGN (FIRST DRAFT)
What we needed before coding

**Users Table**
- id (UUID)
- name
- email(unique)
- password_hash
- role(user/ADMIN)
- created_at

**Uploads Table**
- id(UUID)
- user_id(FK)
- image_path
- image_hash
- status(PENDING/VERIFIED/ SUSPICIOUS)
- fraud_score
- created_at

**ExtractedTransactions table**
- id
- upload_id(FK)
- transaction_id
- amount 
- sender_name
- reciver_name
- transaction_date
- raw_text

**FraudRepors Table**
- id 
- upload_id
- duplicate_flag(boolean)
- anomly_flag(boolean)
- confidence_score
- explanation

## 🧠 5️⃣ DATA FLOW (Important for Understanding)
when user uplads:
1. file stored
2. Image hashed(SHA256)
3. OCR extracts text
4. Text parsec into fields
5. Fraud rules run
6. Fraud score calculated
7. Data saved
8. Response returned

#### 🎯 NOW WE ACTUALLY START CODING

### 🔵 [MONTH 1 – BACKEND FOUNDATION](./Month1.md)