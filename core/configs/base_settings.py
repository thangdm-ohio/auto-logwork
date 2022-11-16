# from kink import di
from functools import cache
from typing import Union
from pydantic import BaseSettings

class APISettings(BaseSettings):
    jira_domain: Union[str, None] = None
    jira_user_uri: Union[str, None] = None
    jira_issue_uri: Union[str, None] = None
    jira_logwork_uri: Union[str, None] = None

    
    class Config:
        env_file = '.env'

class APIConfigs(BaseSettings):

    description = """
    This is the api for log work faster than jira
    """

    responses = {
        404: {'description': 'Not Found'},
        400: {'description': 'Cannot process further'}
    }

    api_metadata = {
        'title': 'Log Work API',
        'description': description,
        'version': '0.0.1',
        'contact': {
            'name': 'ThangDM (Toby Doan)',
            'email': 'thangdm@ohio-digital.com'
        },
        'responses': responses
    }

@cache
def get_setting():
    return APISettings()

@cache
def get_configs():
    return APIConfigs()