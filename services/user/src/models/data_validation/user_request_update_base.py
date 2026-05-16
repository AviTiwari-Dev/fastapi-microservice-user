"""

"""

from datetime import date
from typing import Annotated

from pydantic import BaseModel, Field, ConfigDict, field_validator

from ...enums.gender import GenderEnum


class UserRequestUpdateBase(BaseModel):
    """
    
    """

    first_name: Annotated[
        str | None,
        Field(
            title="First Name",
            description="First Name",
            deprecated=False,
            min_length=1,
            max_length=25,
            pattern=r"^[a-zA-Z]+$",
            strict=True,
        )
    ] = None
    middle_name: Annotated[
        str | None,
        Field(
            title="First Name",
            description="First Name",
            deprecated=False,
            min_length=0,
            max_length=25,
            pattern=r"^[a-zA-Z]*$",
            strict=True,
        )
    ] = None
    last_name: Annotated[
        str | None,
        Field(
            title="First Name",
            description="First Name",
            deprecated=False,
            min_length=0,
            max_length=25,
            pattern=r"^[a-zA-Z]*$",
            strict=True,
        )
    ] = None
    date_of_birth: Annotated[
        date | None,
        Field(
            title="Date of Birth",
            description="Date of Birth",
            deprecated=False,
            strict=False,
        )
    ] = None
    gender: Annotated[
        GenderEnum | None,
        Field(
            title="Gender",
            description="Gender",
            deprecated=False,
            strict=False,
        )
    ] = None

    model_config = ConfigDict(
        extra="forbid",
    )

    @field_validator("first_name", "middle_name", "last_name", mode="after")
    @classmethod
    def normalize_full_name(cls, value: str) -> str:
        return value.lower() if value else value
