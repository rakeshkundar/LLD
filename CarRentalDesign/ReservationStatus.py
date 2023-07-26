import enum

class ReservationStatus(enum):
    SCHEDULED = 1
    INPROGRESS = 2
    COMPLETED = 3
    CANCELLED = 4