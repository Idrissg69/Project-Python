from fastapi import FastAPI

from Projet.core.database import Base, engine
from Projet.models.book import Book
from Projet.models.author import Author
from Projet.routes.book import router as book_router
from Projet.routes.author import router as author_router



app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(book_router)
app.include_router(author_router)

