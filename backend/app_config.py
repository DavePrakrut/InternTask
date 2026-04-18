import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"


def _load_env_file(path: Path) -> None:
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ[key.strip()] = value.strip().strip('"').strip("'")


_load_env_file(ENV_FILE)


class Settings(BaseSettings):
    database_url: str = "sqlite:///./task_manager.db"
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    model_config = SettingsConfigDict(case_sensitive=False, extra="ignore")


settings = Settings(
    database_url=os.environ.get("DATABASE_URL", "sqlite:///./task_manager.db"),
    jwt_secret_key=os.environ.get("JWT_SECRET_KEY", ""),
    jwt_algorithm=os.environ.get("JWT_ALGORITHM", "HS256"),
    access_token_expire_minutes=int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", "60")),
)
