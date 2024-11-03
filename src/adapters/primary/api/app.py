from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.adapters.primary.api.movies import routes as MovieRoutes
from src.adapters.primary.api.users import routes as UserRoutes

app = FastAPI(
    title="FavoritesFilmsService",
    description="Сервис для управления фильмами",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UserRoutes.router, tags=['Пользователи'])
app.include_router(MovieRoutes.router, tags=['Фильмы'], prefix='/movies')
