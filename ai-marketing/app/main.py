from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()

app = FastAPI(
    title="Topnine AI Marketing API",
    version="0.1.0",
    description="Marketing, advertising and SEO agent platform for Topnine Sport.",
)


@app.get("/health", tags=["operations"])
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "topnine-ai-marketing", "environment": settings.app_env}


@app.get("/", tags=["operations"])
def root() -> dict[str, str]:
    return {
        "name": "Topnine AI Marketing",
        "status": "bootstrap",
        "message": "API foundation is running. Integrations are not enabled yet.",
    }
