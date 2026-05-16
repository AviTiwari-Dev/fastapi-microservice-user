"""

"""

from datetime import date, datetime, timezone
from uuid import UUID, uuid7

from sqlalchemy import Date, DateTime, Enum, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from ...bases.user import UserBase
from ...enums.gender import GenderEnum


class User(UserBase):
    """
    
    """
    __tablename__ = "users"
    __table_args__ = {"schema": "user_schema"}

    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid7,
    )
    first_name: Mapped[str] = mapped_column(
        String(25),
        nullable=False,
    )
    middle_name: Mapped[str] = mapped_column(
        String(25),
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String(25),
        nullable=False,
    )
    date_of_birth: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )
    gender: Mapped[GenderEnum] = mapped_column(
        Enum(GenderEnum, name="genderenum"),
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
