from typing import Type

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session as SessionModel
from sqlalchemy.orm import sessionmaker

from config import settings

engine = create_engine(settings.database_uri)


Session: Type[SessionModel] = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


Base = declarative_base()


def get_db() -> SessionModel:
    session = Session()
    try:
        yield session
        session.commit()
    finally:
        session.close()
