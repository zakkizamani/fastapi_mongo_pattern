from pydantic import BaseModel


class Pagination(BaseModel):
    page: int = 0
    size: int = 10
    sort: str = "createTime"
    dir: int = -1
