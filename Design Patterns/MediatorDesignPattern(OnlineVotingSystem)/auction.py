from mediator_interface import MediatorInterface
from bidder_interface import BidderInterface
from threading import RLock

class Auction(MediatorInterface):
    bidders: list

    def __init__(self, price=0.0) -> None:
        self.bidders = []
        self.lock = RLock()
        self.auction_price = price

    def add_bidder(self, bidder: BidderInterface):
        with self.lock:
            self.bidders.append(bidder)

    def place_bid(self, amount: float):
        # Double Locking mechanism for synchronization purpose
        if(amount > self.auction_price):
            with self.lock:
                if(amount > self.auction_price):
                    self.auction_price = amount
                    for bidder in self.bidders:
                        bidder.receive_bid_notification(amount)
    