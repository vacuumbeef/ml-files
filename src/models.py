from pydantic import BaseModel


class CreateFileOut(BaseModel):
    link: str


class FileExistsOut(BaseModel):
    exists: bool
