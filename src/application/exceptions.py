from dataclasses import dataclass

from fastapi import HTTPException


# Ошибки, связанные с пользователем
@dataclass
class InvalidCredentialsException(HTTPException):
    detail: str = "Неверный пароль."
    status_code: int = 409


@dataclass
class UserNotFoundException(HTTPException):
    detail: str = "Пользователь не найден."
    status_code: int = 404


@dataclass
class NotAuthorizedException(HTTPException):
    detail: str = "Вы не авторизованы."
    status_code: int = 401


@dataclass
class AlreadyAuthorizedException(HTTPException):
    detail: str = "Вы уже авторизованы."
    status_code: int = 401


@dataclass
class UserExistsException(HTTPException):
    detail: str = "Пользователь уже существует."
    status_code: int = 409


# Ошибки, связанные с фильмом
@dataclass
class FilmAlreadyExistsException(HTTPException):
    detail: str = "Фильм уже в избранном."
    status_code: int = 409
    

@dataclass
class FilmNotFoundException(HTTPException):
    detail: str = "Фильм не найден."
    status_code: int = 404
