# ===== Module & Library
from typing import Any

# ===== Header

# ===== Function

# ===== Class
class MongoTemplate:
    """
    Class for creating mongo find query.

    Detail function:
    - Is    : Exact search.
    - Eq    : Equal search.
    - In    : In search.
    - Nin   : Not in search.
    - All   : All search.
    - Gt    : Greater than search.
    - Lt    : Less than search.
    - Gte   : Greater than equal search.
    - Lte   : Less than equal search.
    - Regex : Regex search.
    """

    def __init__(self):
        self.__criteria = []
        self.__field = None

    def where_(self, field: str):
        self.__field = field
        return self

    def is_(self, key: Any):
        if self.__field not in ["", None]:
            self.__criteria.append({self.__field: key})

    def eq_(self, key: Any):
        if self.__field not in ["", None]:
            self.__criteria.append({self.__field: {"$eq": key}})

    def ne_(self, key: Any):
        if self.__field not in ["", None]:
            self.__criteria.append({self.__field: {"$ne": key}})

    def in_(self, key: Any):
        if self.__field not in ["", None]:
            if isinstance(key, list):
                self.__criteria.append({self.__field: {"$in": key}})
            else:
                self.__criteria.append({self.__field: {"$in": [key]}})

    def nin_(self, key: Any):
        if self.__field not in ["", None]:
            if isinstance(key, list):
                self.__criteria.append({self.__field: {"$nin": key}})
            else:
                self.__criteria.append({self.__field: {"$nin": [key]}})

    def all_(self, key: Any):
        if self.__field not in ["", None]:
            if isinstance(key, list):
                self.__criteria.append({self.__field: {"$all": key}})
            else:
                self.__criteria.append({self.__field: {"$all": [key]}})

    def gt_(self, key: Any):
        if self.__field not in ["", None]:
            self.__criteria.append({self.__field: {"$gt": key}})

    def lt_(self, key: Any):
        if self.__field not in ["", None]:
            self.__criteria.append({self.__field: {"$lt": key}})

    def gte_(self, key: Any):
        if self.__field not in ["", None]:
            self.__criteria.append({self.__field: {"$gte": key}})

    def lte_(self, key: Any):
        if self.__field not in ["", None]:
            self.__criteria.append({self.__field: {"$lte": key}})

    def regex_(self, key: str):
        if self.__field not in ["", None]:
            self.__criteria.append({self.__field: {"$regex": key, "$options": "i"}})

    def create_criteria(self):
        if len(self.__criteria) > 0:
            return {"$and": self.__criteria}
        else:
            return {}


# ===== Class
