from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic
import uvicorn
from presentation import single
from core.configs.base_response import BaseResponse
from core.configs.base_settings import get_setting

app = FastAPI(**get_setting().api_metadata, dependencies=[Depends(HTTPBasic())], default_response_class=BaseResponse)

@app.on_event('startup')
async def startup():
    # get_setting()
    return


app.include_router(single)

uvicorn.Config(app, reload=True)