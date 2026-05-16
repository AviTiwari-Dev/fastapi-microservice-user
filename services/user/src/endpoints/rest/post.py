"""

"""

from fastapi import Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from ...dependencies.get_session import get_session
from ...models.data_validation.user_request_base import UserRequestBase
from ...models.data_validation.user_response import UserResponse
from ...operations.add_user_data import add_user_data
from ...routers.user import router as user_router


@user_router.post(
    path="/",
    name="Create User",
    deprecated=False,
    include_in_schema=True,
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def post_user(
    user: UserRequestBase,
    session: AsyncSession = Depends(get_session),
):
    """
    Create user data
    """
    return await add_user_data(**user.model_dump(), session=session)
