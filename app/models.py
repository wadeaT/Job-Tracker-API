from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class User(Base):
    __tablename__ = "users"

    """
    the table should have the following columns:
    id (Integer, auto-numbered, pk)
    email (varchar)
    password_hash (varchar)
    """

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]


