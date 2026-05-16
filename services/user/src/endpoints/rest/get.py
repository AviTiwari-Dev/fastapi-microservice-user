"""

"""

from uuid import UUID

from fastapi import Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession

from ...dependencies.get_session import get_session
from ...models.data_validation.user_response import UserResponse
from ...operations.retrieve_user_data import retrieve_user_data
from ...routers.user import router as user_router


@user_router.get(
    path="/",
    name="Get User",
    deprecated=False,
    include_in_schema=True,
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
)
async def get_user(
    user_id: UUID,
    session: AsyncSession = Depends(get_session),
):
    """
    
    """
    user = await retrieve_user_data(user_id=user_id, session=session)

    if user is None:
        raise HTTPException(
            detail="User not found",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    
    return user
