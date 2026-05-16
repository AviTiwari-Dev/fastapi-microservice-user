"""

"""

from datetime import date
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from ..enums.gender import GenderEnum
from ..exceptions.user_not_found_error import UserNotFoundError
from ..models.data_storage.user import User


async def update_user_data(
    user_id: UUID,
    first_name: str | None,
    middle_name: str | None,
    last_name: str | None,
    date_of_birth: date | None,
    gender: GenderEnum | None,
    session: AsyncSession,
) -> User:
    """
    
    """
    user = await session.get(User, user_id)

    if user is None:
        raise UserNotFoundError("User Not Found")
    
    if first_name is not None:
        user.first_name = first_name
    
    if middle_name is not None:
        user.middle_name = middle_name
    
    if last_name is not None:
        user.last_name = last_name
    
    if date_of_birth is not None:
        user.date_of_birth = date_of_birth
    
    if gender is not None:
        user.gender = gender
    
    await session.flush()
    await session.refresh(user)

    return user
