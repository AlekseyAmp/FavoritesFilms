from fastapi import APIRouter, Depends

from src.adapters.primary.api.movies.dependencies import get_movie_service
from src.adapters.primary.api.movies.schemas import FavoriteMovieSchema
from src.adapters.primary.api.users.dependencies import get_user_id
from src.application.movie.services import MovieService

router = APIRouter()


@router.get(
    "/search",
    response_model=dict,
    summary="Поиск фильмов",
    dependencies=[Depends(get_user_id)]
)
async def search_fim(
    query: str,
    movie_service: MovieService = Depends(get_movie_service),
) -> dict:
    return await movie_service.search_film(query=query)


@router.post(
    "/favorites",
    response_model=FavoriteMovieSchema,
    summary="Добавление фильма в избранное"
)
async def add_film_to_favorite(
    kinopoisk_id: int,
    user_id: int = Depends(get_user_id),
    movie_service: MovieService = Depends(get_movie_service),
) -> FavoriteMovieSchema:
    return await movie_service.add_film_to_favorite(
        kinopoisk_id=kinopoisk_id,
        user_id=user_id
    )


@router.get(
    "/favorites",
    response_model=list[FavoriteMovieSchema],
    summary="Получение списка избранных фильмов"
)
async def get_favorites(
    user_id: int = Depends(get_user_id),
    movie_service: MovieService = Depends(get_movie_service),
) -> list[FavoriteMovieSchema]:
    return await movie_service.get_favorites(user_id=user_id)


@router.get(
    "/{kinopoisk_id}",
    response_model=dict,
    summary="Получение деталей фильма",
    dependencies=[Depends(get_user_id)]
)
async def get_film(
    kinopoisk_id: int,
    movie_service: MovieService = Depends(get_movie_service),
) -> dict:
    return await movie_service.get_film(kinopoisk_id=kinopoisk_id)


@router.delete(
    "/favorites/{kinopoisk_id}",
    response_model=dict[str, str],
    summary="Удаление фильма из избранного"
)
async def delete_film_from_favorite(
    kinopoisk_id: int,
    user_id: int = Depends(get_user_id),
    movie_service: MovieService = Depends(get_movie_service),
) -> dict[str, str]:
    kinopoisk_id = await movie_service.delete_film_from_favorite(
        kinopoisk_id=kinopoisk_id,
        user_id=user_id
    )

    if kinopoisk_id:
        return {"message": "Фильм удален из избранного"}
