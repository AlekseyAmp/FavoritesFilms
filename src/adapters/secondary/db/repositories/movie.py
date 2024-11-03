from dataclasses import asdict, dataclass

import sqlalchemy as sqla

from src.adapters.secondary.db.repositories import BaseRepository
from src.adapters.secondary.db.tables import favorite_movies
from src.application.movie import entities, interfaces


@dataclass
class FavoriteMovieRepository(BaseRepository, interfaces.IFavoriteMovieRepository):
    """
    Репозиторий для работы с любимыми фильмами.
    """
    
    async def add(self, favorite_movie: entities.CreateFavoriteMovie) -> entities.FavoriteMovie:
        """
        Добавление фильма в избранное.

        :param favorite_movie: Объект фильма для добавления в избранное.
        
        :return: Созданный объект фильма.
        """
        
        query = sqla.insert(
            favorite_movies
        ).values(
            asdict(favorite_movie)
        ).returning(favorite_movies)

        result = self.session.execute(query)
        self.session.commit()

        return entities.FavoriteMovie(**result.mappings().one())

    async def get(self, kinopoisk_id: int, user_id: int) -> entities.FavoriteMovie:
        """
        Поиск фильма в избранном.

        :param kinopoisk_id: Идентификатор фильма в Кинопоиске.
        :param user_id: Идентификатор пользователя.

        :return: Объект фильма или None, если не найден.
        """
        
        query = sqla.select(favorite_movies).where(
            favorite_movies.c.kinopoisk_id == kinopoisk_id,
            favorite_movies.c.user_id == user_id
        )

        favorite_movie = self.session.execute(query).mappings().one_or_none()

        return entities.FavoriteMovie(**favorite_movie) if favorite_movie else None
        
    async def list(self, user_id: int) -> list[entities.FavoriteMovie]:
        """
        Возвращает список любимых фильмов.

        :param user_id: Идентификатор пользователя.

        :return: Список фильмов.
        """
        
        query = sqla.select(favorite_movies).where(
            favorite_movies.c.user_id == user_id
        )

        f_movies = self.session.execute(query).mappings().all()

        return [
            entities.FavoriteMovie(**favorite_movie)
            for favorite_movie in f_movies
        ]

    async def delete(self, kinopoisk_id: int, user_id: int) -> int:
        """
        Удаление фильма из избранного.

        :param kinopoisk_id: Идентификатор фильма в Кинопоиске.
        :param user_id: Идентификатор пользователя.
        """

        query = sqla.delete(favorite_movies).where(
            favorite_movies.c.kinopoisk_id == kinopoisk_id,
            favorite_movies.c.user_id == user_id
        )

        self.session.execute(query)
        self.session.commit()

        return kinopoisk_id
