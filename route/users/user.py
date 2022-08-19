from fastapi import APIRouter, Depends, Body
from auth.jwt_handler import signJWT
from auth.jwt_beaerer import jwtBearer
from src.model.user.user import UserPage, UserSuccess
from src.model.user.user_dto import UserDto, UserLoginSchema
from src.model.default.paging import Pagination
from src.model.default.response import SuccessRespone
from util.field.pydantic_object_id import PydanticObjectId
from env.mongo_collection import *

router_user = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

#get Users
@router_user.get("/users", dependencies=[Depends(jwtBearer())])
async def user_get_users(paging: Pagination = Depends(Pagination)):
    _user=[]
    data_user = users.find()
    for data in data_user:
        _user.append(data)
    return str(_user)
 

# get id User
@router_user.get('/users/{username}',dependencies=[Depends(jwtBearer())])
async def user_get_id_users(user_dto: UserDto):
    try:
        result = users.find_one({'username':user_dto})
        if result:
            return str(result)
        return {"Status" : "Data Tidak Ditemukan!"}
    except Exception as e:
        return {"Status" : "Data Tidak Ditemukan!"}

# add User
@router_user.post('/users', dependencies=[Depends(jwtBearer())])
async def user_add_users(user_dto: UserDto):
    result=users.insert_one(user_dto.dict()).inserted_id
    return {
        "status": "success",
        "data" : user_dto
    }

# update User
@router_user.put('/users', dependencies=[Depends(jwtBearer())])
async def user_edit_user(user_dto: UserDto):
    result = users.update_one({'username': user_dto.username}, {'$set':{
        "nama" : user_dto.nama,
        "email" : user_dto.email,
        "phone" : user_dto.phone,
        "address" : user_dto.address,
        "username" : user_dto.username,
        "password" : user_dto.password,
        "status" : user_dto.status,
        "created_time" : user_dto.created_time,
        "updated_time" : user_dto.updated_time,
        "updated_by" : user_dto.updated_by
        }})
    return {
        "status" : "Update Success!",
        "data" : user_dto
    }

# delete User
@router_user.delete('/users/{username}',dependencies=[Depends(jwtBearer())])
async def user_delete_user(user_dto: UserDto):
    result = users.find_one({'username':user_dto})
    if result:
        users.delete_one({'username':user_dto})
        return {
            "status":"Delete Success!"
        }
    else:
        return {"Status" : "Data Tidak Ditemukan!"}


# user signup
# @router_user.post('/user/signup')
# async def user_signup_user(user_dto : UserDto =Body(default=None)):
#     checkUsername = users.find_one({'username':user_dto.username})
#     if not checkUsername:
#         result=users.insert_one(user_dto.dict()).inserted_id
#         return signJWT(user_dto.id, user_dto.username, user_dto.email, user_dto.phone)
#     else:
#         return {"Status" : "Username Sudah Terdaftar!"}
    
# # user Login
# @router_user.post('/user/login')
# async def user_login_login(user: UserLoginSchema =Body(default=None)):
#     checkUserLogin = users.find_one({'username':user.username})
#     if (checkUserLogin):
#         if user.username==checkUserLogin["username"] and  checkUserLogin["password"]==user.password and checkUserLogin["status"]==True:
#             token = signJWT(str(checkUserLogin["_id"]), checkUserLogin["username"], checkUserLogin["email"], checkUserLogin["phone"])
#             return {
#                 "status_code":200,
#                 "message":"Berhasil Login",
#                 "access_token": token,
#                 "data":{
#                     "id":str(checkUserLogin["_id"]),
#                     "nama":checkUserLogin["nama"]
#                 }
#             }
#         elif checkUserLogin["status"] == False:
#             return {"status":"akun tidak aktif"}
#         else:
#             return {"status":"password salah"}
#     else:
#         return {"status":"user data tidak ditemukan"}

