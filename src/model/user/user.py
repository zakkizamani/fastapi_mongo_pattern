from typing import List

from pydantic import Field

from src.model.default.address import UserField
from src.model.default.base import DefaultModel, DefaultPage
from src.model.default.response import SuccessRespone
from util.field.pydantic_object_id import PydanticObjectId


class User(DefaultModel):
    # name: str = None
    # initials: str = None
    user: UserField = None


class UserOnDb(User):
    id: PydanticObjectId = Field(..., alias="_id")


class UserPage(DefaultPage):
    data: List[UserOnDb] = []


class UserSuccess(SuccessRespone):
    data: List[UserOnDb] = []
