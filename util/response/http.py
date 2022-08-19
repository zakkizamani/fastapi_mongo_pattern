from http import HTTPStatus
from typing import Any, Dict, Optional

from fastapi import HTTPException

from src.model.default.response import ErrorResponse
from util.response.enum import (
    BadRequestEnum,
    ForbidenEnum,
    InternalServerErrorEnum,
    NotFoundEnum,
    NotModifiedEnum,
    UnauthorizedEnum,
)


# 3xx
class NotModifiedException(HTTPException):
    def __init__(
        self,
        type: NotModifiedEnum,
        message: str = "",
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        response = ErrorResponse()
        response.status_code = HTTPStatus.NOT_MODIFIED.value
        response.error = HTTPStatus.NOT_MODIFIED.phrase.upper()
        response.type = type
        response.message = message
        super().__init__(HTTPStatus.NOT_MODIFIED.value, response.dict(), headers)


# 4xx
class BadRequestException(HTTPException):
    def __init__(
        self,
        type: BadRequestEnum,
        message: str = "",
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        response = ErrorResponse()
        response.status_code = HTTPStatus.BAD_REQUEST.value
        response.error = HTTPStatus.BAD_REQUEST.phrase.upper()
        response.type = type
        response.message = message
        super().__init__(HTTPStatus.BAD_REQUEST.value, response.dict(), headers)


class UnauthorizedException(HTTPException):
    def __init__(
        self,
        type: UnauthorizedEnum,
        message: str = "",
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        response = ErrorResponse()
        response.status_code = HTTPStatus.UNAUTHORIZED.value
        response.error = HTTPStatus.UNAUTHORIZED.phrase.upper()
        response.type = type
        response.message = message
        super().__init__(HTTPStatus.UNAUTHORIZED.value, response.dict(), headers)


class ForbiddenException(HTTPException):
    def __init__(
        self,
        type: ForbidenEnum,
        message: str = "",
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        response = ErrorResponse()
        response.status_code = HTTPStatus.FORBIDDEN.value
        response.error = HTTPStatus.FORBIDDEN.phrase.upper()
        response.type = type
        response.message = message
        super().__init__(HTTPStatus.FORBIDDEN.value, response.dict(), headers)


class NotFoundException(HTTPException):
    def __init__(
        self,
        type: NotFoundEnum,
        message: str = "",
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        response = ErrorResponse()
        response.status_code = HTTPStatus.NOT_FOUND.value
        response.error = HTTPStatus.NOT_FOUND.phrase.upper()
        response.type = type
        response.message = message
        super().__init__(HTTPStatus.NOT_FOUND.value, response.dict(), headers)


# 5xx
class InternalServerErrorException(HTTPException):
    def __init__(
        self,
        type: InternalServerErrorEnum,
        message: str = "",
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        response = ErrorResponse()
        response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR.value
        response.error = HTTPStatus.INTERNAL_SERVER_ERROR.phrase.upper()
        response.type = type
        response.message = str(message)
        super().__init__(
            HTTPStatus.INTERNAL_SERVER_ERROR.value, response.dict(), headers
        )
