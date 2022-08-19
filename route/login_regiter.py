from fastapi import APIRouter, Depends, Body
from auth.jwt_handler import signJWT
from auth.jwt_beaerer import jwtBearer
from src.model.user.user_dto import UserDto, UserLoginSchema
from env.mongo_collection import *

router = APIRouter()
# user signup
@router.post('/user/signup')
async def user_signup_user(user_dto : UserDto =Body(default=None)):
    checkUsername = users.find_one({'username':user_dto.username})
    if not checkUsername:
        result=users.insert_one(user_dto.dict()).inserted_id
        return signJWT(user_dto.id, user_dto.username, user_dto.email, user_dto.phone)
    else:
        return {"Status" : "Username Sudah Terdaftar!"}
    
# user Login
@router.post('/user/login')
async def user_login_user(user: UserLoginSchema =Body(default=None)):
    checkUserLogin = users.find_one({'username':user.username})
    if (checkUserLogin):
        if user.username==checkUserLogin["username"] and  checkUserLogin["password"]==user.password and checkUserLogin["status"]==True:
            token = signJWT(str(checkUserLogin["_id"]), checkUserLogin["username"], checkUserLogin["email"], checkUserLogin["phone"])
            return {
                "status_code":200,
                "message":"Berhasil Login",
                "access_token": token,
                "data":{
                    "id":str(checkUserLogin["_id"]),
                    "nama":checkUserLogin["nama"]
                }
            }
        elif checkUserLogin["status"] == False:
            return {"status":"akun tidak aktif"}
        else:
            return {"status":"password salah"}
    else:
        return {"status":"user data tidak ditemukan"}
