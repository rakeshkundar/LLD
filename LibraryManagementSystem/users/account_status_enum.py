from __future__ import annotations
from enum import Enum

class AccountStatus(Enum):
    ACTIVE = 0,
    CANCELLED = 1
    BLACKLISTED = 2