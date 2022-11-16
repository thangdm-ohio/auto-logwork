from typing import List
from pydantic import BaseModel, Field
from .Logwork import LogWorkRequest

class SingleRequest(BaseModel):
  # user: User
  issue_code: str = Field(description='COD-13')
  logs: List[LogWorkRequest] = Field(min_items=1)
