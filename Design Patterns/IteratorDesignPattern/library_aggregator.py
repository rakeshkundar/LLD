from aggregator import Aggregator
from book_iterator import BookIterator

class Library(Aggregator):
    books: list

    def __init__(self, books: list) -> None:
        self.books = books

    def createIterator(self):
        return BookIterator(self.books)