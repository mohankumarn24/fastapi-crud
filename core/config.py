# config.py

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class Settings(BaseSettings):

    database_url: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()


## Create a `.env` file in project root
# DATABASE_URL=postgresql://postgres:password@localhost:5432/mydb