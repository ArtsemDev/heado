from fastapi import APIRouter
from fastapi.responses import UJSONResponse


router = APIRouter(
    prefix='/api',
    default_response_class=UJSONResponse,
    include_in_schema=False
)
