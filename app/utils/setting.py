from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    DB_NAME: str
    DB_URL: str

    class Config:
        env_file = ".env"


env_vars = Settings()
