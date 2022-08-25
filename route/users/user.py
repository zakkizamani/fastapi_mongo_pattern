from fastapi import APIRouter, Depends, Body
from auth.jwt_handler import signJWT
from auth.jwt_beaerer import jwtBearer
from src.model.user.user import UserPage, UserSuccess
from src.model.user.user_dto import ErrorResponseModel, UserDto, UserLoginSchema, ResponseModel, userUpdate
from src.model.default.paging import Pagination
from src.model.default.response import SuccessRespone
from util.field.pydantic_object_id import PydanticObjectId
from env.mongo_collection import *
from fastapi.encoders import jsonable_encoder
from src.controller.user.user import (
    retrive_all_users,add_user, retrive_userId, user_update, delete_user
)

router_user = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

#get all Users
@router_user.get("/users", response_description="Added data into user database", dependencies=[Depends(jwtBearer())])
async def get_all_users():
    users = await retrive_all_users()
    if users:
        return ResponseModel(users, "users retrive sucessufly")
    return ResponseModel(users, "Empty list returned")
    

# # add User
@router_user.post('/users', response_description="added data into db users",dependencies=[Depends(jwtBearer())])
async def add_users_data(user : UserDto = Body(...)):
     user =  jsonable_encoder(user)
     new_user = await add_user(user)
     return ResponseModel(new_user, "User add successfuly!") 


# get id User
@router_user.get('/users/{id}', response_description="get user from ID", dependencies=[Depends(jwtBearer())])
async def get_user_id(id):
    user = await retrive_userId(id)
    if user:
        return ResponseModel(user, "User ditemukan!")
    return ErrorResponseModel(user, 404, "user tidak ditemukan")


# update User
@router_user.put('/users/{id}', response_description="Edit data user", dependencies=[Depends(jwtBearer())])
async def update_user_data(id:str, req: userUpdate = Body()):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user= await user_update(id, req)
    if updated_user:
        return ResponseModel(
            'user with ID: {} name update is successful'.format(id),
            'user berhasil di Update'
        )
    return ErrorResponseModel(
        "An error occured",
        404,
        "Error when updating the user data"
    )
    


# # delete User
@router_user.delete('/users/{id}', response_description="delete user by id", dependencies=[Depends(jwtBearer())])
async def delete_user_data(id):
    delete_user_data = await delete_user(id)
    if delete_user_data:
        return ResponseModel(
            "user with ID:{} removed".format(
                id), "user deleted successfuly"
        )   
    return ErrorResponseModel(
        "An erroroccured", 404, "user with id{0} doesn't exist".format(id)
    )
