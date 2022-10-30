# Importing required configurations
from fastapi import APIRouter
from models.user import emp
from config.db import conn 
from schemas.user import userEntity, usersEntity
from bson.objectid import ObjectId

# Initializing router
user = APIRouter()

# GET API to fetch details of all the users from MongoDB
@user.get('/')
async def get_all_users():
    return usersEntity(conn.employee.emp.find())


# GET API to fetch details of a single user by id from MongoDB 
@user.get('/{id}')
async def get_a_user(id):
    return userEntity(conn.employee.emp.find_one({"_id": ObjectId(id)}))


# POST API to create the details or create the documents in MongoDB
@user.post('/')
async def create_user(user: emp):
    conn.employee.emp.insert_one(dict(user))
    return usersEntity(conn.employee.emp.find())


# PUT API to change or updated the selected values of an id in MongoDB
@user.put('/{id}')
async def update_user(id, user: emp):
    conn.employee.emp.find_one_and_update({"_id": ObjectId(id)},{
        "$set": dict(user)
    })
    return userEntity(conn.employee.emp.find_one({"_id": ObjectId(id)}))


# DELETE API to delete the specified id from MongoDB
@user.delete('/{id}')
async def delete_user(id, user: emp):
    return userEntity(conn.employee.emp.find_one_and_delete({"_id": ObjectId(id)}))


