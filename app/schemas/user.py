import datetime

import msgspec


class User(msgspec.Struct, kw_only=True):
    id: int | None = None
    name: str
    surname: str
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None


class UserCreate(msgspec.Struct, kw_only=True):
    name: str
    surname: str
    password: str


class UserUpdate(msgspec.Struct, kw_only=True):
    name: str | None = None
    surname: str | None = None
    password: str | None = None
