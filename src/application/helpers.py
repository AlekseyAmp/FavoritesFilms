from datetime import datetime

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """
    Хеширует пароль.

    :param password: Пароль.

    :return: Хешированный пароль.
    """

    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Проверяет пароль.

    :param password: Обычный пароль.
    :param hashed_password: Хешированный пароль.

    :return: True, если пароли совпадают, иначе False.
    """

    return pwd_context.verify(password, hashed_password)


def get_current_dt() -> datetime:
    """
    Возвращает текущую дату и время.

    :return: Текущая дата и время.
    """

    return datetime.now()