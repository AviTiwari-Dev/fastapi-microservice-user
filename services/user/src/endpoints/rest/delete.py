"""

"""

from uuid import UUID

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ...dependencies.get_session import get_session
from ...exceptions.user_not_found_error import UserNotFoundError
from ...operations.remove_user_data import remove_user_data
from ...routers.user import router as user_router


@user_router.delete(
    path="/",
    name="Delete User",
    deprecated=False,
    include_in_schema=True,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    user_id: UUID,
    session: AsyncSession = Depends(get_session)
):
    try:
        await remove_user_data(
            user_id=user_id,
            session=session,
        )
    except UserNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
