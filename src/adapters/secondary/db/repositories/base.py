from dataclasses import dataclass

from sqlalchemy.orm import Session


@dataclass
class BaseRepository:
    """
    Базовый класс репозитория SQLAlchemy.

    :param session: Сессия SQLAlchemy для взаимодействия с базой данных.
    """

    session: Session
