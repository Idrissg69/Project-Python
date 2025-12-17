from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    isbn: str


class BookResponse(BaseModel):
    id: int
    title: str
    isbn: str

    class Config:
        orm_mode = True
