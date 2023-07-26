from __future__ import annotations
from datetime import datetime

class Book:
    title: str
    publish_date: datetime
    authors: list(str)
    language: str
    no_of_pages: int
    price: float

    def __init__(self, title: str, publish_date: datetime, language: str, no_of_pages:int, authors: list(str), price: float) -> None:
        self.title = title
        self.publish_date = publish_date
        self.language = language
        self.no_of_pages = no_of_pages
        self.authors = authors
        self.price = price

