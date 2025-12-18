from pydantic import BaseModel
from models.categories import BookCategory
from schemas.author import AuthorResponse

class BookCreate(BaseModel):
    title: str
    isbn: str
    author_id: int
    category: BookCategory

class BookResponse(BaseModel):
    id: int
    title: str
    isbn: str
    category: BookCategory
    author: AuthorResponse

    model_config = {
        "from_attributes": True
    }
