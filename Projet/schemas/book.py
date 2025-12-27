from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

from models.categories import BookCategory


class BookCreate(BaseModel):
    title: str
    isbn: str

    year: int = Field(..., ge=1450, le=date.today().year)

    author_id: int

    total_copies: int = Field(..., ge=1)
    available_copies: int = Field(..., ge=0)

    category: BookCategory
    language: str
    pages: int = Field(..., ge=1)
    publisher: str


class BookResponse(BookCreate):
    id: int

    model_config = {
        "from_attributes": True
    }
