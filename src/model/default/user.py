from typing import List
from datetime import date, datetime
from pydantic import BaseModel, Field


class Coordinate(BaseModel):
    type: str = "Point"
    coordinates: List[float] = []


class User(BaseModel):
    id: int = Field(default=None)
    nama : str = Field(default=None)
    email : str = Field(default=None)
    phone : str = Field(default=None)
    address : str = Field(default=None)
    username : str = Field(default=None)
    password : str = Field(default=None)
    status : bool = Field(default=False)
    created_time : datetime = Field(default=None)
    updated_time : datetime = Field(default=None)
    updated_by:str = Field(default=None)
