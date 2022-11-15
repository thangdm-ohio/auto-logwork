# from kink import di
from functools import cache, lru_cache
from pydantic import BaseSettings

class APISettings(BaseSettings):
    description = """
    This is the api for log work faster than jira
    """

    responses = {
        404: {'description': 'Not Found'},
        400: {'description': 'Cannot process further'}
    }

    jira_domain: str
    jira_user_uri: str
    jira_issue_uri: str
    jira_logwork_uri: str

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
    class Config:
        env_file = '.env'

@cache
def get_setting():
    return APISettings()