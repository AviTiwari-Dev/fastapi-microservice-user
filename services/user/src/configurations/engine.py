"""

"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    
    """
    URL: str
    ECHO: bool
    POOL_SIZE: int
    MAX_OVERFLOW: int
    POOL_TIMEOUT: int
    POOL_RECYCLE: int
    FUTURE: bool


    model_config = SettingsConfigDict(
        env_file="./.env",
        extra="ignore",
    )

engine_configuration_variables = Settings()
