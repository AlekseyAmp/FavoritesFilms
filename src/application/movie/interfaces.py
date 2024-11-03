from abc import ABC, abstractmethod

from src.application.movie import entities


class IFavoriteMovieRepository(ABC):

    @abstractmethod
    async def add(self, favorite_movie: entities.CreateFavoriteMovie) -> entities.FavoriteMovie:
        ...

    @abstractmethod
    async def get(self, kinopoisk_id: int, user_id: int) -> entities.FavoriteMovie: ...

    @abstractmethod
    async def list(self, user_id: int) -> list[entities.FavoriteMovie]: ...

    @abstractmethod
    async def delete(self, kinopoisk_id: int, user_id: int) -> int: ...


class IKinopoiskRequest(ABC):

    @abstractmethod
    async def search(self, query: str) -> dict: ...

    @abstractmethod
    async def get(self, kinopoisk_id: int) -> dict: ...
