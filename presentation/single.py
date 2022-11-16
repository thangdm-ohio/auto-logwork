from fastapi import APIRouter, Depends, Request
from core.configs.base_response import BaseResponseModel
from core.configs.base_settings import APISettings, get_setting
from schema.request import TotalRequest
from data import PerformLogwork
from loguru import logger

single = APIRouter(prefix='/single', tags=['single'])

@single.post('/', 
    response_model=BaseResponseModel, 
    description="single log work")
async def create_single_logwork(request: Request, body: TotalRequest, settings: APISettings = Depends(get_setting)):
    parsed_body = body.dict()
    _, failure = await PerformLogwork(settings=settings).single_task_logging(request=request,body=parsed_body)
    if failure:
        return failure
    return BaseResponseModel()