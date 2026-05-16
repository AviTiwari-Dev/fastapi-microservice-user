"""

"""

from typing import Annotated
from uuid import UUID

from pydantic import Field, ConfigDict

from .user_request_base import UserRequestBase


class UserResponse(UserRequestBase):
    """
    
    """
    user_id: Annotated[
        UUID,
        Field(
            title="User ID",
            description="User ID",
            deprecated=False,
            strict=True,
        )
    ]

    model_config = ConfigDict(
        extra="ignore",
    )
