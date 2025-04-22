from fastapi import Request
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String
from typing import List

from app.database import Base
from app.models import Question


class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)

    questions: Mapped[List["Question"]] = relationship(back_populates="topic")
    games: Mapped[List["Game"]] = relationship(back_populates="topic")

    async def _admin_repr__(self, request: Request):
        return self.name