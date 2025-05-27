from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    GROQ_API_KEY : SecretStr

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding='utf-8',
        case_sensitive=False,
    )

    # class Config:
    #     env_file = ".env"
    #     env_file_encoding='utf-8'
    #     case_sensitive = False

settings = Settings()
