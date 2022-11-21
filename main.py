from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic
import uvicorn
from presentation import *
from core.configs.base_response import BaseResponse
from core.configs.base_settings import get_configs, get_setting
from core.configs.security import get_user

app = FastAPI(**get_configs().api_metadata, dependencies=[
    Depends(get_user),
    Depends(get_setting)
    ], default_response_class=BaseResponse)

@app.on_event('startup')
async def startup():
    # get_setting()
    return


app.include_router(single)
app.include_router(multiple)
app.include_router(user)

uvicorn.Config(app, reload=True)