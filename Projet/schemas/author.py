from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class AuthorCreate(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    nationality: str = Field(min_length=2, max_length=2)


class AuthorResponse(AuthorCreate):
    id: int

    model_config = {
        "from_attributes": True
    }
