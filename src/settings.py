from datetime import datetime
from pathlib import Path

from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from .mixins import contact_mixin
from .types import Settings


BASE_DIR = Path(__file__).resolve().parent.parent
SETTINGS = Settings()
static = StaticFiles(directory=BASE_DIR / 'static')
templates = Jinja2Templates(
    directory=BASE_DIR / 'templates',
    context_processors=[contact_mixin]
)
templates.env.globals['datetime'] = datetime
