from datetime import datetime
from typing import Any, List

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    status_code: int = None
    error: str = None
    timestamp: str = datetime.now().isoformat()

    type: str = None
    message: str = None


class SuccessRespone(BaseModel):
    status_code: int = 200
    type: str = None
    message: str = None
    data: List = []
