from file_system import FileSystem


class File(FileSystem):
    file_name: str

    def __init__(self, name: str) -> None:
        self.file_name = name
        
    def ls(self):
        print(f"File Name is : {self.file_name}")