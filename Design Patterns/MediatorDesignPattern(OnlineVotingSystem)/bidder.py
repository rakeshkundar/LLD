from bidder_interface import BidderInterface
from auction import Auction

class Bidder(BidderInterface):
    name: str
    auction: Auction

    def __init__(self, name: str, auction: Auction) -> None:
        self.name = name
        self.auction = auction
        self.auction.add_bidder(self)
        print(f"Bidder {self.name} has been added to the auction")

    def place_bid(self, amount: float):
        self.auction.place_bid(amount)

    def receive_bid_notification(self, amount: float):
        print(f"New Bid place with amount : {amount} in Bidder {self.name}")

    def get_name(self):
        return self.name
