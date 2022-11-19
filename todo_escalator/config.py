from pydantic import BaseSettings, SecretStr


class Config(BaseSettings):
    api_token: SecretStr

    class Config:
        env_file = '../.env'
