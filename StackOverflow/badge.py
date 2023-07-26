class Badge:
    id: str
    name: str
    description: str


    def __init__(self, id: str, name: str, desc: str) -> None:
        self.id = id
        self.name = name
        self.description = desc

        