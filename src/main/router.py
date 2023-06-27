from fastapi import APIRouter
from starlette.responses import HTMLResponse

router = APIRouter(
    default_response_class=HTMLResponse,
    include_in_schema=False
)
