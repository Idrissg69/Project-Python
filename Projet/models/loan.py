from sqlalchemy import Column, Integer, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import date, timedelta
from core.database import Base


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    user_id = Column(Integer, nullable=False)

    loan_date = Column(Date, default=date.today, nullable=False)
    due_date = Column(
        Date,
        default=lambda: date.today() + timedelta(days=14),
        nullable=False
    )
    return_date = Column(Date, nullable=True)
    penalty = Column(Float, default=0.0)

    book = relationship("Book", back_populates="loans")
