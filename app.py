from fastapi import FastAPI

from src.main import router as main_router
from src.api import router as api_router
from src.settings import static


app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
    swagger_ui_parameters=None,
    swagger_ui_init_oauth=None,
    swagger_ui_oauth2_redirect_url=None,
)
app.include_router(router=main_router)
app.include_router(router=api_router)
app.mount(path='/static', app=static, name='static')
