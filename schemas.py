from pydantic import BaseModel
from datetime import date
from typing import List


class Genres(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genres]
    pages: int
