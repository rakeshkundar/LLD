from __future__ import annotations
from user import User
from account_status_enum import AccountStatus
from reservation import Reservation
from book_lending import BookLending
from datetime import datetime
from fine import Fine
from books.book_status_enum import BookStatus

class Member(Account):
    total_checkedout_books: int

    def __init__(self, username: str, password: str, user: User) -> None:
        super().__init__(username, password, user, AccountStatus.ACTIVE)
        self.total_checkedout_books = 0

    def get_total_books_checked_out(self) -> int:
        return self.total_checkedout_books

    def reserve_book(self):
        pass

    def renew_book_item(self, book_item):
        self.check_for_fine(book_item.get_barcode())
        book_reservation = Reservation.fetch_reservation_details(
        book_item.get_barcode())
        # check if self book item has a pending reservation from another member
        if book_reservation != None and book_reservation.get_member_id() != self.get_member_id():
            print("self book is reserved by another member")
            self.decrement_total_books_checkedout()
            book_item.update_book_item_state(BookStatus.RESERVED)
            book_reservation.send_book_available_notification()
            return False
        elif book_reservation != None:
            # book item has a pending reservation from self member
            book_reservation.update_status(ReservationStatus.COMPLETED)

        BookLending.lend_book(book_item.get_bar_code(), self.get_member_id())
        book_item.update_due_date(datetime.datetime.now().AddDays(Constants.MAX_LENDING_DAYS))
        return True

    def increment_total_books_checked_out(self):
        pass

    def return_book_item(self, book_item):
        self.check_for_fine(book_item.get_barcode())
        book_reservation = Reservation.fetch_reservation_details(book_item.get_barcode())
        if book_reservation != None:
            # book item has a pending reservation
            book_item.update_book_item_status(BookStatus.RESERVED)
            book_reservation.send_book_available_notification()
            book_item.update_book_item_status(BookStatus.AVAILABLE)

    def checkout_book_item(self, book_item):
        if self.get_total_books_checked_out() >= 5:
            print("The user has already checked-out maximum number of books")
            return False
        book_reservation = Reservation.fetch_reservation_details(book_item.get_barcode())
        if book_reservation != None and book_reservation.get_member_id() != self.get_id():
            # book item has a pending reservation from another user
            print("self book is reserved by another member")
            return False
        elif book_reservation != None:
            # book item has a pending reservation from the give member, update it
            book_reservation.update_status(ReservationStatus.COMPLETED)

        if not book_item.checkout(self.get_id()):
            return False

        self.increment_total_books_checkedout()
        return True

    def check_for_fine(self, barcode: str):
        book_lending = BookLending.fetch_lending_details(barcode)
        due_date = book_lending.get_due_date()
        today = datetime.date.today()
        # check if the book has been returned within the due date
        if today > due_date:
            diff = today - due_date
            diff_days = diff.days
            Fine.collect_fine(self.get_member_id(), diff_days)
