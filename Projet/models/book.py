from sqlalchemy import Column, Integer, String, ForeignKey
from Projet.core.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=True)

