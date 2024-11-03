from dataclasses import dataclass
from datetime import datetime


@dataclass
class CreateUser:
    username: str
    created_at: datetime
    password: str | None = None


@dataclass
class User(CreateUser):
    id: int | None = None
