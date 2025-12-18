from fastapi import FastAPI

from core.database import Base, engine
from models.book import Book
from models.author import Author
from routes.book import router as book_router
from routes.author import router as author_router



app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(book_router)
app.include_router(author_router)

