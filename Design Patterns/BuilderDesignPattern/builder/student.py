from __future__ import annotations
from builder_interface import BuilderInterface

class Student:
    roll_number: int
    age: int
    name: str
    father_name: str
    mother_name: str
    subjects: list(str)


    def __init__(self, builder: BuilderInterface) -> None:
        self.roll_number = builder.roll_number
        self.age = builder.age
        self.name = builder.name
        self.father_name = builder.father_name
        self.mother_name = builder.mother_name
        self.subjects = builder.subjects


    def to_string(self):
        return f""" Roll No : {self.roll_number} \n Age : {self.age} \n Name : {self.name} \n Father Name : {self.father_name} \n Mother Name : {self.mother_name} \n Subjects : {self.subjects} \n"""