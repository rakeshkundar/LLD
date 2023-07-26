from datetime import datetime


class Bounty:
    reptation: str
    expiry: datetime

    def __init__(self, reputation: str, expiry: datetime) -> None:
        self.reptation = reputation
        self.expiry = expiry

    def modify_reputation(self, reputation: str):
        self.reptation = reputation