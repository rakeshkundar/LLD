from system_enums import AccountStatus

class Account:
    id: str
    password: str
    name: str
    email: str
    phone: str
    status: AccountStatus
    address: str
    reputation: int

    def __init__(self, id: str, password: str, name: str, email: str, phone: str, status: AccountStatus, address: str) -> None:
        self.id = id
        self.password = password
        self.name = name
        self.email = email
        self.phone = phone
        self.status = status
        self.address = address
        self.reputation = 0
        