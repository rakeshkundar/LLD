class Tag:
    id: str
    name: str
    description: str
    weekly_frequency: int
    monthly_frequency: int

    def __init__(self, id: str, name: str, desc: str) -> None:
        self.id = id
        self.name = name
        self.description = desc
        self.weekly_frequency = 0
        self.monthly_frequency = 0