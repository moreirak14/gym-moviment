from __future__ import annotations

from typing import List, Optional, Type, TypeVar

from sqlalchemy.orm.session import Session

from src.commons.abstracts.repository import AbstractRepository

T = TypeVar("T")


class CRUDSqlAlchemyRepository(AbstractRepository[T]):
    def __init__(self, session: Session, obj_type: Type[T]):
        self.session = session
        self.obj_type = obj_type
        self.seen = set()

    def _add(self, obj: T):
        self.session.add(obj)
        self.seen.add(obj)

    def _get(self, **kwargs) -> Optional[T]:
        obj = self.session.query(self.obj_type).filter_by(**kwargs).first()
        self.seen.add(obj)
        return obj

    def list(self) -> List[T]:
        result = self.session.query(self.obj_type).all()

        for obj in result:
            self.seen.add(obj)
        return result
