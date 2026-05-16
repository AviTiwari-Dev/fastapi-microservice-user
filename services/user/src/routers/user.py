"""

"""

from fastapi import APIRouter


router = APIRouter(
    prefix="/user",
    include_in_schema=True,
    deprecated=False,
    tags=["User"],
)
