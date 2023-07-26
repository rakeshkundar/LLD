from director import Director
from engineer_builder import EngineerBuilder
from mba_builder import MBABuilder
from student import Student


if __name__ == '__main__':
    eng_builder: EngineerBuilder = EngineerBuilder()
    mba_builder: MBABuilder = MBABuilder()
    director: Director = Director(mba_builder)
    student: Student = director.create_student()

    print(student.to_string())


    