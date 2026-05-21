from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    COHERE_API_KEY: str

    EMAIL_USER: str
    EMAIL_PASSWORD: str

    class Config:
        env_file = ".env"


settings = Settings()