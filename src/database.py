import asyncio
from typing import Annotated

from sqlalchemy import String, create_engine, text, URL
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker, DeclarativeBase

from config import settings

sync_engine = create_engine (
    url = settings.DATABASE_URL_psycopg,
    echo = True,
    # pool_size=5,
    # max_overflow=10,
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
)

session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

class Base(DeclarativeBase):
    pass




# with engine.connect() as conn:
#     res = conn.execute(text("SELECT VERSION()"))
#     print(f"{res.all()=}")
