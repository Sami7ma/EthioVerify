### 🔵 MONTH 1 – BACKEND FOUNDATION

## Install & Setup what I need to build thsi project
1. Install Node.js ✅
2. Create a new project ✅
3. Setup Express ✅
4. Setup Basic Server ✅
5. Setup PostgresSQl 
6. Connect Database

# WEEK 1 PLAN 
**Day 1:**
- Install Node ✅
- Initalize project ✅
- Create Express Server ✅
- Learn what each line does ✅

**Day 2:**
- Revise HTTP deeply ✅
- Build GET Endpoint ✅
- Buil POST Endpoint ✅

**Day 3:**
- Setup PostgresSQl ✅
- Install Prsima ORM ✅
- Connect DB ✅

**Day 4:**
- Create User Model
- Migrate database
- Insert test user

**Day 5:**
- Build Register endpoint
- hash password with bycrpt
- Test with postman

**Day 6:**
- Build Login Endpoint
- Implement JWT

**Day 7:**
- Review Everything
- Refactor
- Write Documentation

### The backend right know
I need fundamentals first and i need to out server.js
ethioverify/
 └── ethioverify-backend/
      ├── node_modules/
      ├── package.json
      ├── package-lock.json
      └── server.js   ✅ HERE
then it will be updating the backend part too
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
**what i learned so far**
*2/17/2026*
- dependencies vs dev dependencies
- cors policy , Even toop
- why Nodemon
- app listen parts 

*2/18/2026*
- Dependency mismatches
- Major Versin breaking changes
- Runtime configuration chagnes
- ORM architecture diffrense 
- **Prisma** (This one is CLI tool) this is the one runnig 
- npx prisma migrate dev // Reads your schema.prisma
- npx prisma generate // creates sq; migrations generates prismaclient code 
- think of it like the *database BUILDER* // Manges databse stucture 
- **Prism client** This i  what the app uses when you call
- const prisma = new Prismaclien()
- THink of this one as the *databse TALKER*
- Runs nodes in node app and executes queries liek await prisma.user.findMany()
- WHY TWO DIFFERENT jobs
- prisma.config.ts used by prisma CLI 
- prismaCLient() -> run tume config,
- prisma 7 uses its own Rust engine to connect whi all NOde driver, Edge runtime , serverles , custom adapters

***🧠 Quick Concept Summary***
      *Tool*	            *Purpose*
- Prisma CLI	      Builds database
- Prisma Client	      Talks to database
- Adapter	            Tells Prisma HOW to connect
- .env	            Stores secrets
- prisma.config.ts	Used only for migrations

*Data Flows down to db*         *Data flows back up*
- Browser                           PostgreSQL
    ↓                                    ↓
- Express Server                    pg driver
    ↓                                    ↓
- Prisma Client                     Adapter
    ↓                                    ↓
- PrismaPg Adapter                  Prisma Client
    ↓                                    ↓
- pg Driver                         Express
    ↓                                    ↓
- PostgreSQL Database               Browser

*why so many layers*
| Layer         | Responsibility            |
| ------------- | ------------------------- |
| Browser       | Send HTTP                 |
| Express       | Handle API logic          |
| Prisma Client | Convert JS → SQL          |
| Adapter       | Connect Prisma → Driver   |
| pg Driver     | Handle network connection |
| PostgreSQL    | Store & execute data      |
