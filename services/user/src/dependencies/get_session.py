"""

"""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from ..session_factories.user import user_session


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    
    """
    async with user_session() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise
        finally:
            await session.close()
