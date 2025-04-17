import datetime

from advanced_alchemy.extensions.litestar import base
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class UserModel(base.DefaultBase):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    surname: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
