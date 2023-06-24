from pydantic import BaseSettings, Field


class AppSettings(BaseSettings):
    schema_path: str = Field("/openapi.json")
    app_title: str = Field("Warpeve file upload")

    secret_word: str = Field(..., env="SECRET_WORD")
    static_path: str = Field("static")
    files_path: str = Field("files")
