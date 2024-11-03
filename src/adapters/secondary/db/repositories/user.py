from dataclasses import asdict, dataclass
from typing import Literal

import sqlalchemy as sqla

from src.adapters.secondary.db.repositories import BaseRepository
from src.adapters.secondary.db.tables import users
from src.application.user import entities, interfaces


@dataclass
class UserRepository(BaseRepository, interfaces.IUserRepository):
    """
    Репозиторий для работы с пользователями.
    """

    async def add(self, user: entities.CreateUser) -> entities.User:
        """
        Создает нового пользователя в базе данных.

        :param user: Объект пользователя для создания.

        :return: Созданный объект пользователя.
        """

        query = sqla.insert(users).values(asdict(user)).returning(users)
        result = self.session.execute(query)
        self.session.commit()

        return entities.User(**result.mappings().one())

    async def get(
        self,
        by: Literal["id", "username"],
        id: int | None = None,
        username: str | None = None,
    ) -> entities.User | None:
        """
        Возвращает пользователя по указанному критерию (id или username).

        :param by: Критерий поиска (может быть "id" или "username").
        :param id: Идентификатор пользователя.
        :param username: Имя пользователя.

        :return: Объект пользователя или None, если не найден.
        """

        # Построение запроса в зависимости от выбранного критерия
        if by == "id" and id is not None:
            query = sqla.select(users).where(users.c.id == id)
        elif by == "username" and username is not None:
            query = sqla.select(users).where(users.c.username == username)
        else:
            raise ValueError("Необходимо указать допустимый критерий поиска и значение.")

        # Выполняем запрос
        user = self.session.execute(query).mappings().one_or_none()

        return entities.User(**user) if user else None
