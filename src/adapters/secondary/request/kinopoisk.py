from dataclasses import dataclass, field

import httpx

from fastapi import HTTPException

from src.adapters.settings import kinopoisk_settings
from src.application.movie.interfaces import IKinopoiskRequest


@dataclass
class KinopoiskRequest(IKinopoiskRequest):
    """
    Класс для работы с API Кинопоиска.
    """

    headers: dict[str, str] = field(
        default_factory=lambda: {
            "accept": "application/json",
            "X-API-KEY": kinopoisk_settings.KINOPOISK_API_KEY
        }
    )

    async def search(self, query: str) -> dict:
        """
        Поиск фильма.
        
        :param query: Поисковый запрос.
        
        :return: Результат поиска.
        """

        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{kinopoisk_settings.KINOPOISK_API_URLS.get('old')}/films/search-by-keyword?keyword={query}",
                headers=self.headers
            )

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Kinopoisk API error: {response.status_code}",
            )

        return response.json()

    async def get(self, kinopoisk_id: int) -> dict:
        """
        Получение деталей фильма.
        
        :param kinopoisk_id: Идентификатор фильма в Кинопоиске.
        
        :return: Результат поиска.
        """

        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{kinopoisk_settings.KINOPOISK_API_URLS.get('new')}/films/{kinopoisk_id}",
                headers=self.headers
            )

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Kinopoisk API error: {response.status_code}",
            )

        return response.json()
