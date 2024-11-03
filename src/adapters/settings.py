from pydantic_settings import BaseSettings, SettingsConfigDict
from yarl import URL


# ---------------------- Настройки базы данных  ---------------------- 
class DatabaseSettings(BaseSettings):
    DB_HOST: str = "0.0.0.0"
    DB_PORT: int = 5432
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_NAME: str

    @property
    def db_sync_url(self) -> URL:
        return URL.build(
            scheme="postgresql",
            host=self.DB_HOST,
            port=self.DB_PORT,
            user=self.DB_USERNAME,
            password=self.DB_PASSWORD,
            path=f"/{self.DB_NAME}",
        )

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


# ---------------------- Настройки приложения  ---------------------- 
class AppSettings(BaseSettings):
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    RELOAD: bool = False

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


# ---------------------- Настройки авторизации  ---------------------- 
class AuthSettings(BaseSettings):
    JWT_SECRET: str
    JWT_ALGHORITM: str
    JWT_COOKIE_NAME: str = "Authorization"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 3000

    model_config = SettingsConfigDict(env_file=".env", extra="allow")
    

# ---------------------- Настройки Kinopoisk  ---------------------- 
class KinopoiskSettings(BaseSettings):
    KINOPOISK_API_KEY: str
    KINOPOISK_API_URLS: dict[str, str] = {
        "old": "https://kinopoiskapiunofficial.tech/api/v2.1",
        "new": "https://kinopoiskapiunofficial.tech/api/v2.2"
    }

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


db_settings = DatabaseSettings()
app_settings = AppSettings()
auth_settings = AuthSettings()
kinopoisk_settings = KinopoiskSettings()
