from datetime import date, timedelta
from typing import Any, Union
from pydantic import BaseModel

class LogWork(BaseModel):
  attributes: dict = {}
  billableSeconds: str = ""
  worker: str
  comment: Union[str, None] = None
  started: str
  timeSpentSeconds: int
  originTaskId: str
  remainingEstimate: Any = None
  endDate: Union[date, None] = None
  includeNonWorkingDays: bool = False

class LogWorkRequest(BaseModel):
  comment: Union[str, None] = None
  started: date
  total_hours: float
  is_ot: bool = False