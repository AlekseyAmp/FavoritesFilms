from dataclasses import asdict, dataclass

from src.adapters.primary.api.users import schemas
from src.adapters.primary.api.users.security import create_access_token
from src.application import exceptions
from src.application.helpers import (
    get_current_dt,
    get_password_hash,
    verify_password,
)
from src.application.user import entities, interfaces


@dataclass
class UserService:

    user_repository: interfaces.IUserRepository

    async def register_user(self, username: str, password: str) -> entities.User:
        """
        Регистрация нового пользователя.

        :param username: Имя пользователя.
        :param password: Пароль.

        :return: Объект пользователя.
        """

        if await self.user_repository.get(by='username', username=username):
            raise exceptions.UserExistsException

        user_data = entities.CreateUser(
            username=username,
            password=get_password_hash(password),
            created_at=get_current_dt(),
        )

        user = await self.user_repository.add(user=user_data)

        return user

    async def login_user(self, username: str, password: str) -> str:
        """
        Вход пользователя.

        :param username: Имя пользователя.
        :param password: Пароль.

        :return: Токен доступа.
        """
        
        user = await self.user_repository.get(by='username', username=username)

        if not user:
            raise exceptions.UserNotFoundException

        if not verify_password(password=password, hashed_password=user.password):
            raise exceptions.InvalidCredentialsException

        return create_access_token(user=user)

    async def get_user_profile(self, user_id: int) -> schemas.UserSchema:
        """
        Возвращает информацию о текущем аутентифицированном пользователе.

        :param user_id: Идентификатор пользователя.

        :return: Pydantic-модель пользователя.
        """

        user = await self.user_repository.get(by='id', id=user_id)
        
        if not user:
            raise exceptions.UserNotFoundException

        return schemas.UserSchema(**asdict(user))
