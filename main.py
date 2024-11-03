import uvicorn

from src.adapters.settings import app_settings

if __name__ == "__main__":
    uvicorn.run(
        app="src.adapters.primary.api.app:app",
        host=app_settings.APP_HOST,
        port=app_settings.APP_PORT,
        reload=app_settings.RELOAD,
    )
