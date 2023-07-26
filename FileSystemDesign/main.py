from directory import Directory
from file import File
from file_system import FileSystem

""" Composite Design Pattern """


if __name__ == '__main__':
    dir: Directory = Directory('root', [])

    file1: FileSystem = File('KGF')
    dir1: Directory = Directory('Movies', [])
    file2: FileSystem = File('RRR')
    dir.add(file1)
    dir1.add(file2)
    dir.add(dir1)

    dir.ls()