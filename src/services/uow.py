from src.adapters.databases import Session
from src.commons.abstracts.unity_of_work import UnitOfWorkBase

DEFAULT_SESSION_FACTORY = Session


class SqlAlchemyUnitOfWork(UnitOfWorkBase):
    default_session_factory = DEFAULT_SESSION_FACTORY

    def __init__(self, session_factory=None):
        self.session_factory = (
            session_factory
            if session_factory is not None
            else self.default_session_factory
        )

    def __enter__(self):
        self.session = self.session_factory()

    def __exit__(self, *args):
        self.rollback()
        self.session.close()

    def _commit(self):
        self.session.commit()

    def _flush(self):
        self.session.flush()

    def rollback(self):
        self.session.rollback()
