from pathlib import Path
from os import mkdir
from typing import Optional, Union

import aiofiles
from fastapi import HTTPException, UploadFile, Request
from fastapi.responses import FileResponse, HTMLResponse

from config import AppSettings
from src.models import CreateFileOut, FileExistsOut

settings = AppSettings()


def check_app_dirs():
    if not Path(settings.static_path).exists():
        raise Exception(f"Directory not found: '{settings.static_path}'")


def create_dirs():
    dirs_names = [settings.files_path]
    for dir_name in dirs_names:
        if Path(dir_name).exists():
            continue
        mkdir(dir_name)


def _generate_file_path(filename: str) -> str:
    path = Path(settings.files_path) / filename
    i: int = 1
    while path.exists():
        path = path.with_stem(f"{path.stem}_{i}")
        i += 1
    return str(path)


def _generate_file_link(filepath: Union[str, Path], request: Request) -> str:
    return f"{request.url}{filepath}"


def file_exists(file_uid: str) -> FileExistsOut:
    return FileExistsOut(
        exists=(Path(settings.files_path) / file_uid).exists()
    )


async def get_file(file_uid: str):
    path = Path(settings.files_path) / file_uid
    if not path.exists():
        raise HTTPException(404, "File not found")
    return FileResponse(path)


async def save_file(file: UploadFile, secret_word: Optional[str], request: Request) -> CreateFileOut:
    if secret_word != settings.secret_word:
        raise HTTPException(401, "Invalid secret word")
    filepath = _generate_file_path(file.filename)
    async with aiofiles.open(filepath, "wb") as f:
        await f.write(await file.read())
    return CreateFileOut(link=_generate_file_link(filepath, request))


def get_static(name: str) -> Union[FileResponse, HTMLResponse]:
    path = Path(settings.static_path) / name
    if not path.exists():
        return HTMLResponse("Not found", 404)
    return FileResponse(path)
