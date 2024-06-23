from sqlalchemy import BigInteger, String, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=True)
    status: Mapped[str] = mapped_column(String, default="user")
    lang: Mapped[str] = mapped_column(String, default="en")

    def is_admin(self, super: bool = False):
        status = ("admin", "super_admin") if super else ("admin")
        return self.status in status

    @classmethod
    async def get_or_create(
        cls,
        session: AsyncSession,
        id: int,
        name: str,
        username: str = None,
        lang: str = "en",
    ):
        stmt = select(cls).where(cls.id == id)
        obj = await session.scalar(stmt)
        if not obj:
            obj = cls(id=id, name=name, username=username, lang=lang)
            session.add(obj)
            await session.flush()
        session.expunge_all()
        return obj
