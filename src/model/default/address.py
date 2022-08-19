from typing import List

from pydantic import BaseModel


class Coordinate(BaseModel):
    type: str = "Point"
    coordinates: List[float] = []


class UserField(BaseModel):
    id: int | None
    nama : str | None
    email : str | None
    phone : str | None
    address : str | None
    username : str | None
    password : str | None
    status : bool | None
    # created_time : datetime | None
    # updated_time : datetime | None
    updated_by:str | None
