from pydantic import BaseModel, Field
from datetime import date, datetime
from src.model.default.address import UserField


class UserDto(BaseModel):
    id: int | None
    nama : str | None
    email : str | None
    phone : str | None
    address : str | None
    username : str | None
    password : str | None
    status : bool | None
    created_time : datetime | None
    updated_time : datetime | None
    updated_by:str | None
    
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
