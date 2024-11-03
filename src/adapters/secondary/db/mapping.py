from sqlalchemy.orm import registry

from src.adapters.secondary.db.tables import favorite_movies, users
from src.application.movie.entities import FavoriteMovie
from src.application.user.entities import User

mapper = registry()

mapper.map_imperatively(User, users)
mapper.map_imperatively(FavoriteMovie, favorite_movies)
