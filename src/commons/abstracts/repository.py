import abc
from typing import Generic, List, Optional, Set, Type, TypeVar

T = TypeVar("T")


class AbstractRepository(abc.ABC, Generic[T]):
    seen: Set[T]
    not_found_exception: Type[Exception] = KeyError

    def __getitem__(self, key) -> T:
        obj = self.get(id=key)
        if obj is None:
            raise self.not_found_exception

        return obj

    def add(self, obj: T):
        self._add(obj)
        self.seen.add(obj)

    def get(self, **kwargs) -> Optional[T]:
        obj = self._get(**kwargs)
        if obj:
            self.seen.add(obj)
        return obj

    @abc.abstractmethod
    def _add(self, obj: T):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, **kwargs) -> T:
        raise NotImplementedError

    @abc.abstractmethod
    def list(self) -> List[T]:
        raise NotImplementedError
