from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # DB_HOST: str
    # DB_PORT: int
    # DB_USER: str
    # DB_PASS: str
    # DB_NAME: str

    @property
    def DATABASE_URL_asyncpg(self):
        # postgresql+asyncpg://postgres:postgres@localhost:5432/sa
        return f"sqlite+aiosqlite:///db.sqlite3"
        
    @property
    def DATABASE_URL_psycopg(self):
        # DSN
        # postgresql+psycopg://postgres:postgres@localhost:5432/sa
        return f"sqlite+pysqlite:///db.sqlite3"
    
#     model_config = SettingsConfigDict(env_file=".env")

settings = Settings()