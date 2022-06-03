from pydantic import BaseSettings


class Settings(BaseSettings):
    api_url: str = "http://test.com"