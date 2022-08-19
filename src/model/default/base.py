from datetime import datetime
from typing import List

from pydantic import BaseModel

from src.model.default.paging import Pagination
from util.field.pydantic_object_id import PydanticObjectId


class DefaultModel(BaseModel):
    createTime: datetime = None
    creatorId: PydanticObjectId = None
    creatorName: str = None

    updateTime: datetime = None
    updaterId: PydanticObjectId = None
    updaterName: str = None

    deleteTime: datetime = None
    deleterId: PydanticObjectId = None
    deleterName: str = None
    isDelete: bool = False

    companyId: PydanticObjectId = None


class DefaultPage(BaseModel):
    status_code: int = 200
    type: str = None
    message: str = None
    data: List = []
    paging: Pagination
