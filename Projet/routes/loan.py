from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from core.database import get_db
from models.loan import Loan
from models.book import Book
from schemas.loan import LoanCreate, LoanResponse

router = APIRouter(prefix="/loans", tags=["Loans"])

MAX_ACTIVE_LOANS = 5
PENALTY_PER_DAY = 1.0


@router.post("/", response_model=LoanResponse)
def borrow_book(data: LoanCreate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == data.book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book.available_copies <= 0:
        raise HTTPException(status_code=400, detail="No available copies")

    active_loans = (
        db.query(Loan)
        .filter(Loan.user_id == data.user_id, Loan.return_date.is_(None))
        .count()
    )

    if active_loans >= MAX_ACTIVE_LOANS:
        raise HTTPException(status_code=400, detail="Maximum number of active loans reached")

    loan = Loan(book_id=data.book_id, user_id=data.user_id)

    book.available_copies -= 1

    db.add(loan)
    db.commit()
    db.refresh(loan)

    return loan


@router.post("/{loan_id}/return", response_model=LoanResponse)
def return_book(loan_id: int, db: Session = Depends(get_db)):
    loan = db.query(Loan).filter(Loan.id == loan_id).first()

    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")

    if loan.return_date:
        raise HTTPException(status_code=400, detail="Book already returned")

    loan.return_date = date.today()

    if loan.return_date > loan.due_date:
        delay = (loan.return_date - loan.due_date).days
        loan.penalty = delay * PENALTY_PER_DAY

    loan.book.available_copies += 1

    db.commit()
    db.refresh(loan)

    return loan
