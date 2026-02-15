### The backend right know
I need fundamentals first and i need to out server.js
ethioverify/
 └── ethioverify-backend/
      ├── node_modules/
      ├── package.json
      ├── package-lock.json
      └── server.js   ✅ HERE
then it will be updating the backend part too..

ethioverify-backend/
 ├── node_modules/
 ├── package.json
 ├── server.js
 └── src/
      ├── controllers/
      ├── services/
      ├── routes/
      ├── middlewares/
      ├── utils/
      ├── config/
      └── prisma/
### what does each folder mean
**📂 controllers/**
handles incomig requests
Example:
UserController.js

It receives request → calls service → sends response.
Think of it as:
- The manager of incoming traffic.
**📂 services/**
this is where teh business logic lives.(DSA)
Example:
FraudDetection.js

THis contains:
- FraudScoring
- OCR logic
- Parsing Logic

