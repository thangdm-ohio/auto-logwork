from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic
import uvicorn
from presentation import single
from core.configs.base_response import BaseResponse
from core.configs.base_settings import get_configs
from core.configs.security import get_user

app = FastAPI(**get_configs().api_metadata, dependencies=[Depends(get_user)], default_response_class=BaseResponse)

@app.on_event('startup')
async def startup():
    # get_setting()
    return


app.include_router(single)

uvicorn.Config(app, reload=True)