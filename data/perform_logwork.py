import typing
from loguru import logger
from core.configs.base_settings import BaseSettings

class PerformLogwork:

    def __init__(self, settings: BaseSettings):
        logger.info(settings.jira_issue_uri)
        self.cfg = settings


    async def single_task_logging(self, body: dict) -> typing.Tuple[typing.Any, typing.Union[int, None]]:
        logger.info(self.cfg.__dict__)
        # logger.info(f'jira_domain: {self.cfg.jira_domain}')
        return None, None