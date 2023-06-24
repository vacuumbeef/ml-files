from typing import Optional, Union
from fastapi import FastAPI, Response, Header, UploadFile, Request
from fastapi.responses import FileResponse, HTMLResponse

from config import AppSettings
from src import business

settings = AppSettings()
app = FastAPI(title=settings.app_title, openapi_url=settings.schema_path)


@app.on_event("startup")
async def startup_event():
    business.check_app_dirs()
    business.create_dirs()


@app.get("/")
async def index() -> Union[FileResponse, HTMLResponse]:
    return business.get_static("index.html")


@app.get("/files/{file_uid}")
async def get_file(file_uid: str) -> Response:
    return await business.get_file(file_uid)


@app.post("/")
async def save_file(request: Request, file: UploadFile, x_secret_word: Optional[str] = Header(...)):
    return await business.save_file(file, x_secret_word, request)


@app.get("/static/{name}")
async def get_static_file(name: str):
    return business.get_static(name)
