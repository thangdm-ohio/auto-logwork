import asyncio
import functools
import json
import typing
from fastapi import Request
from loguru import logger
import requests
from core.configs.base_settings import APISettings, get_setting
from core.configs.base_response import Failure, Internal, Bad
from schema.request.Logwork import LogWork

class PerformLogwork:

    def __init__(self, settings: APISettings):
        self.cfg = settings
        self.loop = asyncio.get_running_loop()


    async def single_task_logging(self, request: Request, body: dict) -> typing.Tuple[typing.Any, typing.Union[Failure, None]]:
        authentication: str = request.headers.get('Authorization')
        issue_id = await self.__get_issue_id(authentication, body.get('issue_code'))
        for item in body.get('logs'):
            logwork_body = LogWork(
                worker=request.state._state.get('user_key'),
                started=str(item.get('started')),
                timeSpentSeconds=round(item.get('total_hours') * 3600),
                originTaskId=issue_id,
                includeNonWorkingDays=item.get('is_ot')
            )

            await self.__log_work(authentication, logwork_body.dict())

        return None, None

    async def __get_issue_id(self, basic_auth: str, issue_key: str) -> typing.Union[str, Failure]:
        try:
            headers = {
                'Content-Type': 'application/json',
                'Authorization': basic_auth
            }

            found = (await self.loop.run_in_executor(
                None,
                functools.partial(
                    requests.get,
                    url=f'{get_setting().jira_domain}{get_setting().jira_issue_uri.format(issue_key=issue_key)}',
                    headers=headers)
                )
            )
            if found.status_code != 200:
                raise Bad(found.content)
            return found.json().get('id')
        except Exception as ex:
            logger.exception(str(ex), ex)
            raise Internal(str(ex))


    async def __log_work(self, basic_auth: str, body: dict):
        logger.info(f'body: {json.dumps(body)}')
        try:
            headers = {
                'Content-Type': 'application/json',
                'Authorization': basic_auth
            }

            response = (await self.loop.run_in_executor(
                None,
                functools.partial(
                    requests.post,
                    url=f'{get_setting().jira_domain}{get_setting().jira_logwork_uri}',
                    headers=headers,
                    data=json.dumps(body)
                )
            ))
            if response.status_code != 200:
                raise Bad(response.content)
            logger.info(response.json())
            return response.json()
        except Exception as ex:
            logger.exception(str(ex), ex)
            raise Internal(str(ex))