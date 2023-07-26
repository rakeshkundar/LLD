from enum import Enum


class AccountStatus(Enum):
    ACTIVE = 0
    BLOCKED = 1
    CANCELLED = 2
    CLOSED =3



class QuestionStatus(Enum):
    OPEN = 0
    DELETED = 1
    CLOSED = 2



class QuestionClosingRemark(Enum):
    DUPLICATE = 0
    OFF_TOPIC = 1
    TOO_BROAD = 2
    NOT_CONSTRUCTIVE = 3
    NOT_A_REAL_QUESTION = 4
    PRIMARILY_OPINION_BASED = 5
    
