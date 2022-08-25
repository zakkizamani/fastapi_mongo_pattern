from pydantic import BaseModel, Field, EmailStr
from fastapi import FastAPI, Query
from datetime import date, datetime
# from src.model.default.address import UserField
from typing import Optional


class UserDto(BaseModel):
    # id: int | None
    nama : str = Query(min_length=3, max_length=50)
    email : EmailStr = Field(...) 
    phone : str | None
    address : str | None
    username : str
    password : str 
    status : bool | None
    created_time : datetime | None
    updated_time : datetime | None
    updated_by:str | None
    
class userUpdate(BaseModel):
    nama : str | None = Query(min_length=3, max_length=50)
    email : EmailStr | None
    phone : str | None
    address : str | None
    username : str | None
    password : str | None
    status : bool | None
    created_time : datetime | None
    updated_time : datetime | None
    updated_by:str | None
    
    class Config:
        schema_extra = {
            "example":{
                "nama" : "Hapus Juka tidak igin di update",
                "email" : "Hapus Juka tidak igin di update",
                "phone" : "Hapus Juka tidak igin di update",
                "address" : "Hapus Juka tidak igin di update",
                "username" : "Hapus Juka tidak igin di update",
                "password" : "Hapus Juka tidak igin di update",
                "status" : "Hapus Juka tidak igin di update",
                "created_time" : "Hapus Juka tidak igin di update",
                "updated_time" : "Hapus Juka tidak igin di update",
                "updated_by":"Hapus Juka tidak igin di update",
            }
        }

class UserLoginSchema(BaseModel):
    username : str = Field(default=None)
    password : str = Field(default=None)
    class Config:
        schema_extra={
            "user register":{
                "username":"jhon_doe",
                "password" : "12345678"
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }
    
def user_helper(users) -> dict:
    return {
        "id": str(users["_id"]),
        "nama": users["nama"],
        "email" :users["email"],
        "phone" : users["phone"],
        "address" : users["address"],
        "username" : users["username"],
        "password" : users["password"],
        "status" : users["status"],
        "created_time" : users["created_time"],
        "updated_time" : users["updated_time"],
        "updated_by":users["updated_by"]
        }
    
def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }