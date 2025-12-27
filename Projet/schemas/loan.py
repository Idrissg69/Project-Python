from pydantic import BaseModel
from datetime import date
from typing import Optional


class LoanCreate(BaseModel):
    book_id: int
    user_id: int


class LoanResponse(BaseModel):
    id: int
    book_id: int
    user_id: int
    loan_date: date
    due_date: date
    return_date: Optional[date]
    penalty: float

    model_config = {
        "from_attributes": True
    }
