from __future__ import annotations

class BuilderInterface:
    roll_number: int
    age: int
    name: str
    father_name: str
    mother_name: str
    subjects: list(str)


    def set_roll_number(self, roll: int):
        self.roll_number = roll
        return self

    def set_age(self, age: int):
        self.age = age
        return self

    def set_name(self, name: str):
        self.name = name
        return self

    def set_father_name(self, name: str):
        self.father_name= name
        return self

    def set_mother_name(self, name: str):
        self.mother_name= name
        return self

    def set_subject(self, subject: list(str)):
        self.subject= subject
        return self

