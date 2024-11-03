from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    UniqueConstraint,
)

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column(
        "id",
        Integer,
        primary_key=True,
        comment="Идентификатор"
    ),
    Column(
        "username",
        String(50),
        unique=True,
        nullable=False,
        comment="Имя пользователя"
    ),
    Column(
        "password",
        String,
        nullable=False,
        comment="Захешированный пароль пользователя"
    ),
    Column(
        "created_at",
        DateTime,
        nullable=False,
        comment="Дата и время создания записи"
    ),
)

favorite_movies = Table(
    "favorite_movies",
    metadata,
    Column(
        "id",
        Integer,
        primary_key=True,
        comment="Идентификатор"
    ),
    Column(
        "user_id",
        ForeignKey(
            'users.id',
            name='user_id_fkey',
            ondelete='CASCADE',
            onupdate='CASCADE'
        ),
        nullable=False,
        comment="Идентификатор пользователя"
    ),
    Column(
        "kinopoisk_id",
        Integer,
        nullable=False,
        comment="Идентификатор фильма на кинопоиске"
    ),
    Column(
        "added_at",
        DateTime,
        nullable=False,
        comment="Дата и время добавления фильма в избранное"
    ),
    UniqueConstraint(
        "user_id",
        "kinopoisk_id",
        name="uq_user_favorite_movie"
    ),
)
