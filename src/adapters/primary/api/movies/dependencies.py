from sqlalchemy.orm import Session

from fastapi import Depends

from src.adapters.secondary.db.repositories import FavoriteMovieRepository
from src.adapters.secondary.db.session import get_session
from src.adapters.secondary.request import KinopoiskRequest
from src.application.movie.services import MovieService


def get_favorite_movie_repository(
    session: Session = Depends(get_session)
) -> FavoriteMovieRepository:
    return FavoriteMovieRepository(session=session)


def get_kinopoisk_request() -> KinopoiskRequest:
    return KinopoiskRequest()


def get_movie_service(
    favorite_movie_repository: FavoriteMovieRepository = Depends(
        get_favorite_movie_repository
    ),
    kinopoisk_request: KinopoiskRequest = Depends(get_kinopoisk_request),
) -> MovieService:
    return MovieService(
        favorite_movie_repository=favorite_movie_repository,
        kinopoisk_request=kinopoisk_request,
    )
