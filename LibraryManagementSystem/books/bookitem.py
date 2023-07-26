from __future__ import annotations
from book import Book
from datetime import datetime
from book_status_enum import BookStatus
from book_lending import BookLending

class BookItem(Book):
    barcode: str
    is_reference_only: bool
    borrowed_date: datetime
    due_date: datetime
    status: BookStatus

    def __init__(self, title: str, publish_date: datetime, language: str, no_of_pages: int, authors: list(str), price: float, barcode: str, is_reference_only: bool, borrowed_date: datetime, due_date: datetime, status: BookStatus) -> None:
        super().__init__(title, publish_date, language, no_of_pages, authors, price)
        self.barcode = barcode
        self.is_reference_only = is_reference_only
        self.borrowed_date = borrowed_date
        self.due_date = due_date
        self.status = status

    def checkout(self, member_id):
        if self.is_reference_only:
            print("This book is for reference only. Cannot be lended")
            return False
        
        if not BookLending.lend_book(self.get_barcode(), member_id):
            return False

        self.update_book_item_status(BookStatus.LOANED)
        return True

