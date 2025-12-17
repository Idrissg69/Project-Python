from pydantic import BaseModel
from .author import AuthorResponse
from Projet.models.book import BookCategory
from Projet.schemas.author import AuthorResponse
from Projet.models.categories import BookCategory
from Projet.schemas.author import AuthorResponse


class BookCreate(BaseModel):
    title: str
    isbn: str
    author_id: int | None = None
    category: BookCategory = BookCategory.AUTRE


class BookResponse(BaseModel):
    id: int
    title: str
    isbn: str
    category: BookCategory
    author: AuthorResponse | None

    class Config:
        orm_mode = True
