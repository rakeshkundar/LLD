from enum import Enum

class OrderStatus(Enum):
    UNSHIPPED = 0
    PENDING = 1
    SHIPPED = 2
    COMPLETED = 3
    CANCELLED = 4
    REFUNDAPPLIED = 5


class AccountStatus(Enum):
    ACTIVE = 0
    BLOCKED = 1
    BANNED = 2
    UNKNOWN = 3


class ShipmentStatus(Enum):
    PENDING = 0
    SHIPPED = 1
    OUTFORDELIVERY = 2
    DELIVERED = 3
    ONHOLD = 4


class PaymentStatus(Enum):
    UNPAID = 0
    PENDING = 1
    COMPLETED = 2
    FAILED = 3
    DECLINED = 4
    CANCELLED = 5
    ABANDONED = 6
    SETTLING = 7
    SETTLED = 8
    REFUNDED = 9