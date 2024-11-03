from sqlalchemy.orm import Session

from fastapi import Depends, Request

from src.adapters.primary.api.users.security import verify_token
from src.adapters.secondary.db.repositories import UserRepository
from src.adapters.secondary.db.session import get_session
from src.adapters.settings import auth_settings
from src.application import exceptions
from src.application.user.services import UserService


def get_user_repository(
    session: Session = Depends(get_session)
) -> UserRepository:
    return UserRepository(session=session)


def get_user_service(
    user_repository: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(user_repository=user_repository)


def check_user_already_authenticated(request: Request) -> None:
    """
    Проверяет авторизован ли пользователь, если да,
    то выбрасывает исключение.

    :param request: Запрос.
    """

    token = request.cookies.get(auth_settings.JWT_COOKIE_NAME)

    if token:
        raise exceptions.AlreadyAuthorizedException()


def get_user_id(
    request: Request,
) -> int:
    """
    Возвращает id пользователя из куки.

    :param request: Запрос.

    :return: Id пользователя.
    """

    token = request.cookies.get(auth_settings.JWT_COOKIE_NAME)

    if not token:
        raise exceptions.NotAuthorizedException

    user = verify_token(token)

    return user['id']
