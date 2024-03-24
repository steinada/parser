import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    login: str
    password: str
    start_url: str

    class Config:
        env_file = '.env'


settings = Settings()
