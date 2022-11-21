from fastapi import APIRouter, Depends, Request
from core.configs.base_response import BaseResponseModel

user = APIRouter(prefix='/user', tags=['user'])

@user.post(
    '/login', 
    response_model=BaseResponseModel,
    description='Precheck the login')
async def auth_precheck():
    return BaseResponseModel(message='success')