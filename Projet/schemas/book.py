from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    isbn: str
    author_id: int | None = None


class BookResponse(BaseModel):
    id: int
    title: str
    isbn: str

    class Config:
        orm_mode = True
