
from datetime import datetime
from typing import Any

from pydantic import BaseModel


class ClientResponseModel(BaseModel):
    requestTime: datetime = None
    method: str = None
    urlRequest: str = None
    requestParam: Any = None
    headers: Any = None
    statusCode: int = None
    contentType: str = None
    responseHeaders: Any = None
    responseBody: Any = None
    responseTime: datetime = None