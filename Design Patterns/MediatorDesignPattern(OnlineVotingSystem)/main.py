from auction import Auction
from bidder import Bidder

if __name__ == '__main__':
    auction = Auction()

    bidder1 = Bidder("1", auction)
    bidder2 = Bidder("2", auction)
    bidder3 = Bidder("3", auction)

    bidder1.place_bid(2)
    bidder2.place_bid(1)

