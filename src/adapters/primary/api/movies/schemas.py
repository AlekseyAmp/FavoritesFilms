from datetime import datetime

from pydantic import BaseModel


class FavoriteMovieSchema(BaseModel):
    id: int
    kinopoisk_id: int
    added_at: datetime
