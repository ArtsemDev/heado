import ujson
from pydantic import BaseConfig
from pydantic import BaseModel as Base


class Config(BaseConfig):
    json_loads = ujson.loads
    json_dumps = ujson.dumps
    orm_mode = True


class BaseModel(Base):
    Config = Config
