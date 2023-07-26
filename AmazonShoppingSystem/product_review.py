from __future__ import annotations
from accounts.member import Member

class ProductReview:
    rating: int
    review: str
    reviewed_by: Member

    def __init__(self, rating: int, review: str, reviewed_by: Member) -> None:
        self.rating = rating
        self.review = review
        self.reviewed_by = reviewed_by

        