from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Projet.models.author import Author
from Projet.schemas.author import AuthorCreate, AuthorResponse
from Projet.core.database import get_db

router = APIRouter(prefix="/authors", tags=["Authors"])
