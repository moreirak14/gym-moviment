from __future__ import annotations

import abc


class UnitOfWorkBase(abc.ABC):
    def __enter__(self) -> UnitOfWorkBase:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    def flush(self):
        self._flush()

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError

    @abc.abstractmethod
    def _flush(self):
        raise NotImplementedError
