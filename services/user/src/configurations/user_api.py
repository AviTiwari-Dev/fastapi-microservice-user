"""

"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    
    """
    DEBUG: bool

    model_config = SettingsConfigDict(
        env_file="./.env",
        extra="ignore",
    )

user_api_configuration_variables = Settings()
