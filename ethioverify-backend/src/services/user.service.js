// user.service.js
const prisma = require('../lib/prisma');
const bcrypt = require('bcrypt');

async function createUser(data) {   // ✅ make sure it's "createUser"
    const hashedPassword = await bcrypt.hash(data.password, 10);
    return prisma.user.create({
        data: {
            email: data.email,
            name: data.name,
            password: hashedPassword,
            role: data.role || 'USER'
        }
    });
}

async function getUser() {
    return prisma.user.findMany({
        select:{
            id: true,
            name: true,
            email: true,
            role:true,
            createdAt: true,   
        }
    })
}

module.exports = {
    createUser,
    getUser
}