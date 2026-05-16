"""

"""

from datetime import date

from sqlalchemy.ext.asyncio import AsyncSession

from ..enums.gender import GenderEnum
from ..models.data_storage.user import User


async def add_user_data(
    session: AsyncSession,
    first_name: str,
    middle_name: str,
    last_name: str,
    date_of_birth: date,
    gender: GenderEnum,
) -> User:
    """
    
    """
    user = User(
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        date_of_birth=date_of_birth,
        gender=gender,
    )

    session.add(user)
    await session.flush()
    await session.refresh(user)

    return user
