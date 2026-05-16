"""

"""

from uuid import UUID

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ...dependencies.get_session import get_session
from ...exceptions.user_not_found_error import UserNotFoundError
from ...models.data_validation.user_request_update_base import UserRequestUpdateBase
from ...models.data_validation.user_response import UserResponse
from ...operations.update_user_data import update_user_data
from ...routers.user import router as user_router


@user_router.patch(
    path="/",
    name="Patch User",
    deprecated=False,
    include_in_schema=True,
    response_model=UserResponse,
    status_code=status.HTTP_200_OK
)
async def patch_user(
    user_id: UUID,
    user: UserRequestUpdateBase,
    session: AsyncSession = Depends(get_session),
):
    """
    
    """
    try:

        updated_user = await update_user_data(
            user_id=user_id,
            session=session,
            first_name=user.first_name,
            middle_name=user.middle_name,
            last_name=user.last_name,
            date_of_birth=user.date_of_birth,
            gender=user.gender,
        )

        return updated_user

    except UserNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
