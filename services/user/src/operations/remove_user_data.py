"""

"""

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from ..exceptions.user_not_found_error import UserNotFoundError
from ..models.data_storage.user import User


async def remove_user_data(
    user_id: UUID,
    session: AsyncSession
):
    """
    
    """
    user = await session.get(User, user_id)

    if user is None:
        raise UserNotFoundError("User not found")

    await session.delete(user)
    await session.flush()
