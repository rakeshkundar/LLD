from __future__ import annotations
from file_system import FileSystem

class Directory(FileSystem):
    directory_name: str
    file_system_list: list(FileSystem)

    def __init__(self, name:str, file_system_list: list(FileSystem)) -> None:
        self.directory_name = name
        self.file_system_list = file_system_list

    def add(self, file_system: FileSystem):
        self.file_system_list.append(file_system)

    def ls(self):
        print(f"Directory name : {self.directory_name}")

        for item in self.file_system_list:
            item.ls()