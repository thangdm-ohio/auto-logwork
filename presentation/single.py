from fastapi import APIRouter, Depends, Request
from core.configs.base_response import BaseResponseModel
from core.configs.base_settings import BaseSettings, get_setting
from schema.request import TotalRequest
from data import PerformLogwork
from loguru import logger

single = APIRouter(prefix='/single', tags=['single'])

@single.post('/', 
    response_model=BaseResponseModel, 
    description="single log work")
async def create_single_logwork(request: Request, body: TotalRequest, settings: BaseSettings = Depends(get_setting)):
    logger.info(f"Authorization: {request.headers.get('Authorization')}")
    parsed_body = body.dict()
    response = await PerformLogwork(settings=settings).single_task_logging(body=parsed_body)
    return BaseResponseModel()