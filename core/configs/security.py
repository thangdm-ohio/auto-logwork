import requests
from fastapi import Depends, Request
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from loguru import logger
from core.configs.base_response import PermissionDenied
from core.configs.base_settings import get_setting

async def get_user(request: Request,credentials: HTTPBasicCredentials = Depends(HTTPBasic())):

  headers = {
    'Content-Type': 'application/json',
    'Authorization': request.headers.get('Authorization')
  }

  authorized = requests.get(f'{get_setting().jira_domain}{get_setting().jira_user_uri.format(username=credentials.username)}', headers=headers)
  if authorized.status_code != 200:
    raise PermissionDenied(f'Please check your account again, if your credentials wrong greater than 3 times, login at this link: {get_setting().jira_domain}/login.jsp to bypass the capcha first')
  
  request.state.username = credentials.username
  request.state.user_key = authorized.json().get('key')
  pass