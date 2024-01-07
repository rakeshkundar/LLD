from __future__ import annotations
from builder_interface import BuilderInterface
from student import Student

class MBABuilder(BuilderInterface):

    def __init__(self) -> None:
        self.roll_number = None
        self.age = None
        self.name = None
        self.father_name = None
        self.mother_name = None
        self.subjects = []

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

    def build(self):
        return Student(self)