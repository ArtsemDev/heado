from sqlalchemy import create_engine, Column, INT
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, declared_attr, DeclarativeBase

from src.settings import SETTINGS


class Base(DeclarativeBase):
    __app_name__: str = 'base'

    id = Column(INT, primary_key=True)

    _sync_engine = create_engine(SETTINGS.DATABASE_URL)
    sync_session = sessionmaker(bind=_sync_engine)

    _async_engine = create_async_engine(SETTINGS.DATABASE_URL['postgresql+asyncpg'])
    async_session = async_sessionmaker(bind=_async_engine)

    @declared_attr
    def __tablename__(self):
        return self.__app_name__ + ''.join(f'_{i.lower()}' if i.isupper() else i for i in self.__name__)
