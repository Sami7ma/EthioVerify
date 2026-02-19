const userServices = require('../services/user.service')

async function createUser(req, res) {
    try {
        const user = await userServices.createUser(req.body)
        res.status(201).json(user)
    }catch(error){
        res.status(500).json({error: error.message})
    }
}

async function getUsers(req, res) {
    try{
        const users = await userServices.getUser()
        res.json(users)
    }catch(error){
        res.status(500).json({error: error.message})
    }
    
}
module.exports = {
  createUser,
  getUsers
}