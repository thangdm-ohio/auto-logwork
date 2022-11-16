import typing
from fastapi import BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class BaseResponseModel(BaseModel):
    status: int = 200
    message: typing.Union[str, None] = None
    data: typing.Any = None

    class Config:
        exclude_none = True

class Failure(HTTPException):
    status: int

    def __init__(self, message):
        super().__init__(status_code=self.status, detail=message, headers=None)

class Internal(Failure):
    status = 500

class Bad(Failure):
    status = 400

class NotFound(HTTPException):
    status = 404

class PermissionDenied(Failure):
    status = 403

class BaseResponse(JSONResponse):
    def __init__(
        self,
        content: typing.Any,
        status_code: int = 200,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        media_type: typing.Optional[str] = None, 
        background: typing.Optional[BackgroundTasks] = None) -> None:
            if isinstance(content, BaseResponseModel) and content.status != status_code:
                status_code = content.status

            super().__init__(content, status_code, headers, media_type, background)