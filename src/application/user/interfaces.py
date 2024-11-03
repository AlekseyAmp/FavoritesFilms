from abc import ABC, abstractmethod
from typing import Literal

from src.application.user import entities


class IUserRepository(ABC):

    @abstractmethod
    def add(self, user: entities.CreateUser) -> entities.User: ...

    @abstractmethod
    def get(
        self,
        by=Literal["id", "username"],
        id: int | None = None,
        username: str | None = None,
    ) -> entities.User: ...
