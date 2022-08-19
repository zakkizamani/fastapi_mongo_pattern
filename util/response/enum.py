from enum import Enum


# Enum Response Message for error status code 2xx
class SuccessEnum(str, Enum):
    OK = "OK"
    SUCCESS_CREATED = "SUCCESS_CREATED"
    SUCCESS_UPDATED = "SUCCESS_UPDATED"


# Enum Response Message for error status code 3xx
# 304
class NotModifiedEnum(str, Enum):
    NOT_MODIEFIED = "NOT_MODIFIED"


# 307
class Redirection(str, Enum):
    TEMPORARY_REDIRECT = "TEMPORARY_REDIRECT"


# Enum Response Message for error status code 4xx
# 400
class BadRequestEnum(str, Enum):
    BAD_REQUEST = "BAD_REQUEST"
    INVALID_DATE_FORMAT = "INVALID_DATE_FORMAT"
    INVALID_PHONE_NUMBER = "INVALID_PHONE_NUMBER"
    INVALID_EMAIL = "INVALID_EMAIL"
    INVALID_OBJECT_ID = "INVALID_OBJECT_ID"
    INVALID_PASSWORD_LENGTH = "INVALID_PASSWORD_LENGHT"

    # service failed to request to another service
    FAILED_TO_REQUEST = "FAILED_TO_REQUEST"


# 401
class UnauthorizedEnum(str, Enum):
    UNAUTHORIZED = "UNATHORIZED"


# 403
class ForbidenEnum(str, Enum):
    ACCESS_FORBIDDEN = "ACCESS_FORBIDDEN"


# 404
class NotFoundEnum(str, Enum):
    NOT_FOUND = "NOT_FOUND"


# Enum Response Message for error status code 5xx
class InternalServerErrorEnum(str, Enum):
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
