require('dotenv').config()
const express = require('express');
const cors = require('cors');
const prisma = require('./lib/prisma');
const userRoutes = require('./routes/user.routes');
const authRoutes = require('./routes/auth.routes');

const app = express();
app.use(cors())
app.use(express.json());
app.use('/users', userRoutes)
app.use('/auth', authRoutes)

const PORT  = process.env.PORT || 5000
app.get('/',(req,res)=>{
    res.send('Ethioverify API Running');
})

app.get('/test-db', async (req,res)=>{
    try{
        const result = await prisma.$queryRaw`SELECT 1`
        res.json({message: "Database connected ", result})
    }catch(error){
        console.error(error)
        res.status(500).json({error: "Database connection failed"})
    }
})

app.listen(PORT,()=>{
    console.log(`Server running on port ${PORT}`);
})