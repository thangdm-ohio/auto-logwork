from io import StringIO
import typing
from fastapi import APIRouter, Request, UploadFile
from core.configs.base_response import BaseResponseModel
from schema.request import SingleRequest, LogWorkRequest
from data import PerformLogwork
from loguru import logger

multiple = APIRouter(prefix='/multiple', tags=['multiple'])

@multiple.post('/',
    response_model=BaseResponseModel, 
    description="log multiple tasks")
async def log_multiple_tasks(request: Request, body: typing.List[SingleRequest]):
    parsed_body = [item.dict() for item in body]
    _, failure = await PerformLogwork().multiple_log_work(request=request,body=parsed_body)
    if failure:
        return failure
    return BaseResponseModel()

@multiple.post('/csv',
    response_model=BaseResponseModel, 
    description="log multiple tasks with csv")
async def csv_log_multiple_tasks(request: Request, csv_file: UploadFile):
    import csv

    all_tasks = {}
    csv_reader = csv.DictReader(
        csv_file.file.read().decode('utf-8').split('\n'),
        delimiter=',',
    )
    for row in csv_reader:
        if row.get('issue_code') not in all_tasks:
            all_tasks[row.get('issue_code')] = []
        all_tasks[row.get('issue_code')].append(LogWorkRequest(**row))

    logger.info(f'all_tasks: {all_tasks}')
    parsed_body = []
    for key, value in all_tasks.items():
        parsed_body.append(SingleRequest(issue_code=key, logs=value).dict())

    _, failure = await PerformLogwork().multiple_log_work(request=request, body=parsed_body)
    if failure:
        return failure

    return BaseResponseModel()
