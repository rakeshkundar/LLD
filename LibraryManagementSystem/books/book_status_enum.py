from enum import Enum

class BookStatus(Enum):
    AVAILABLE = 0
    RESERVED = 1
    LOANED = 2
    LOST = 3