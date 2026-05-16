"""

"""

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from ..models.data_storage.user import User


async def retrieve_user_data(
    user_id: UUID,
    session: AsyncSession,
) -> User:
    """
    
    """
    return await session.get(User, user_id)
