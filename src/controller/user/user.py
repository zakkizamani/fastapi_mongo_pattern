from ast import Return
from env.mongo_collection import *
from src.model.user.user_dto import ResponseModel, user_helper
from bson.objectid import ObjectId
from util.field.pydantic_object_id import PydanticObjectId


# retrive all data
async def retrive_all_users():
    # return str(TBL_USER.find())
    users = []
    async for student in TBL_USER.find():
        users.append(user_helper(student))
    return users

# add_user
async def add_user(one_user: dict) -> dict:
    user = await TBL_USER.insert_one(one_user)
    new_user = await TBL_USER.find_one({"_id":user.inserted_id})
    # return new_user
    return user_helper(new_user)


# get user by id
async def retrive_userId(id:str)-> dict:
    user = await TBL_USER.find_one({"_id": PydanticObjectId(id)})
    if user:
        return user_helper(user)
    
async def user_update(id: str, data: dict):
    if len(data) < 1:
        return False
    
    user = await TBL_USER.find_one({"_id": PydanticObjectId(id)})
    if user:
        user_change = await TBL_USER.update_one(
            {"_id":PydanticObjectId(id)}, {"$set":data}
        )
        
        if user_change:
            return True
        return False

async def delete_user(id:str):
    user = await TBL_USER.find_one({"_id":PydanticObjectId(id)})
    if user:
        await TBL_USER.delete_one({"_id":PydanticObjectId(id)})
        return True
    
    # penambahancontroller