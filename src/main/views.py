from starlette.requests import Request
from starlette.responses import HTMLResponse

from .router import router
from ..settings import templates


@router.get('/', name='main_index', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        name='/main/index.html',
        context={
            'request': request,
        }
    )


@router.get('/contact', name='main_contact', response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse(
        name='/main/contact.html',
        context={
            'request': request
        }
    )
