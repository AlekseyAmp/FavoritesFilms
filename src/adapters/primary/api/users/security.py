from typing import Any

from jose import jwt

from src.adapters.settings import auth_settings
from src.application.user import entities


def create_access_token(user: entities.User) -> str:
    """
    Создает токен доступа для пользователя.

    :param user: Объект пользователя.

    :return: Токен доступа.
    """

    try:
        payload = {
            "id": user.id,
            "username": user.username
        }
        return jwt.encode(
            payload,
            key=auth_settings.JWT_SECRET,
            algorithm=auth_settings.JWT_ALGHORITM
        )
    except Exception as e:
        return f"Ошибка при создании токена: {str(e)}"


def verify_token(token: str) -> dict[str, Any] | str:
    """
    Проверяет токен доступа.

    :param token: Токен доступа.

    :return: Полезная нагрузка токена.
    """

    try:
        payload = jwt.decode(
            token=token,
            key=auth_settings.JWT_SECRET
        )
        return payload
    except Exception as e:
        return f"Ошибка при проверке токена: {str(e)}"
