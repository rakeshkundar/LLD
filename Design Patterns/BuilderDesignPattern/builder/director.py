from builder_interface import BuilderInterface
from engineer_builder import EngineerBuilder
from mba_builder import MBABuilder
from student import Student

class Director(BuilderInterface):
    builder: BuilderInterface

    def __init__(self, builder: BuilderInterface) -> None:
        self.builder = builder


    def create_student(self):
        if(isinstance(self.builder, EngineerBuilder)):
            return self.create_engineer_student()
        elif(isinstance(self.builder, MBABuilder)):
            return self.create_mba_student()
        else:
            return None


    def create_engineer_student(self):
        return Student(self.builder.set_roll_number(1).set_age(10).set_name('Rakesh'))

    
    def create_mba_student(self):
        return Student(self.builder.set_roll_number(1).set_age(10).set_name('Rakesh').set_father_name('Narayan').set_mother_name('Sujatha'))
        
    