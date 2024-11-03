from dataclasses import asdict, dataclass

from src.adapters.primary.api.movies import schemas
from src.application import exceptions
from src.application.helpers import get_current_dt
from src.application.movie import entities, interfaces


@dataclass
class MovieService:

    favorite_movie_repository: interfaces.IFavoriteMovieRepository
    kinopoisk_request: interfaces.IKinopoiskRequest

    async def search_film(self, query: str) -> dict:
        """
        Поиск фильма.
        
        :param query: Поисковый запрос.
        
        :return: Результат поиска.
        """
        
        return await self.kinopoisk_request.search(query=query.lower().strip())

    async def add_film_to_favorite(self, kinopoisk_id: int, user_id: int) -> schemas.FavoriteMovieSchema:
        """
        Добавление фильма в избранное.

        :param kinopoisk_id: Идентификатор фильма в Кинопоиске.
        :param user_id: Идентификатор пользователя.

        :return: Результат добавления.
        """

        film = await self.kinopoisk_request.get(kinopoisk_id=kinopoisk_id)

        if film:
            if await self.favorite_movie_repository.get(kinopoisk_id=kinopoisk_id, user_id=user_id):
                raise exceptions.FilmAlreadyExistsException
            
            favorite_movie = entities.CreateFavoriteMovie(
                kinopoisk_id=kinopoisk_id,
                added_at=get_current_dt(),
                user_id=user_id,
            )

            created_favorite_movie = await self.favorite_movie_repository.add(
                favorite_movie=favorite_movie
            )

            return schemas.FavoriteMovieSchema(**asdict(created_favorite_movie))

    async def get_film(self, kinopoisk_id: int) -> dict:
        """
        Получение деталей фильма.

        :param kinopoisk_id: Идентификатор фильма в Кинопоиске.

        :return: Результат поиска.
        """

        return await self.kinopoisk_request.get(kinopoisk_id=kinopoisk_id)

    async def get_favorites(self, user_id: int) -> list[schemas.FavoriteMovieSchema]:
        """
        Возвращает список любимых фильмов.

        :param user_id: Идентификатор пользователя.

        :return: Список фильмов.
        """

        favorite_movies = await self.favorite_movie_repository.list(user_id=user_id)

        return [
            schemas.FavoriteMovieSchema(**asdict(favorite_movie))
            for favorite_movie in favorite_movies    
        ]

    async def delete_film_from_favorite(self, kinopoisk_id: int, user_id: int) -> int:
        """
        Удаление фильма из избранного.

        :param kinopoisk_id: Идентификатор фильма в Кинопоиске.
        :param user_id: Идентификатор пользователя.

        :return: Идентификатор удаляемого фильма.
        """

        if not await self.favorite_movie_repository.get(kinopoisk_id=kinopoisk_id, user_id=user_id):
            raise exceptions.FilmNotFoundException

        await self.favorite_movie_repository.delete(
            kinopoisk_id=kinopoisk_id,
            user_id=user_id
        )

        return kinopoisk_id
