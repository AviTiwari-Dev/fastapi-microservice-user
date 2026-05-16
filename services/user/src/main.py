"""

"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from . import endpoints
from .bases.user import UserBase
from .configurations.user_api import user_api_configuration_variables
from .engines.user import user_engine
from .routers.user import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    
    """
    async with user_engine.begin() as connection:
        await connection.run_sync(UserBase.metadata.create_all)
    yield


user_api = FastAPI(
    title="User API",
    version="0.1",
    debug=user_api_configuration_variables.DEBUG,
    deprecated=False,
    description="User api",
    summary="User api service",
    include_in_schema=True,
    docs_url="/documentation/Swagger",
    redoc_url="/documentation/ReDoc",
    openapi_url="/documentation/openapi.json",
    lifespan=lifespan,
    contact={
        "name": "Avi Tiwari",
        "email": "email@example.com",
    },
    license_info={
        "name": "MIT License",
        "identifier": "MIT",
    },
)

user_api.include_router(user_router)
