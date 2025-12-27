from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship

from core.database import Base
from models.categories import BookCategory


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    year = Column(Integer, nullable=False)

    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)

    total_copies = Column(Integer, nullable=False)
    available_copies = Column(Integer, nullable=False)

    category = Column(Enum(BookCategory), nullable=False)
    language = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    publisher = Column(String, nullable=False)

    author = relationship("Author", back_populates="books")
    loans = relationship("Loan", back_populates="book")
