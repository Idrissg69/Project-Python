from sqlalchemy import Column, Integer, String, Date, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from core.database import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    date_of_birth = Column(Date, nullable=False)
    nationality = Column(String(2), nullable=False) 

    books = relationship("Book", back_populates="author")

    __table_args__ = (
        UniqueConstraint("first_name", "last_name", name="uq_author_fullname"),
    )
