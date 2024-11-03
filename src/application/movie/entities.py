from dataclasses import dataclass
from datetime import datetime


@dataclass
class CreateFavoriteMovie:
    kinopoisk_id: int
    added_at: datetime
    user_id: int | None = None


@dataclass
class FavoriteMovie(CreateFavoriteMovie):
    id: int | None = None
