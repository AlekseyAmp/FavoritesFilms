from datetime import datetime

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: str
    created_at: datetime
