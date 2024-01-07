from __future__ import annotations
from collections import deque

class ObjectPool:
    __pool: deque

    def __init__(self, size: int) -> None:
        self.__pool = deque()
        self.__size = size
        self.initialize(size)

    def create():
        pass

    def initialize(self, size: int):
        print(f"Initializing Object pool ....")
        
        for _ in range(size):
            self.__pool.append(self.create())

    def borrow_object(self):
        obj = self.__pool.popleft()

        if(obj is None):
            obj = self.create()
        
        return obj
    
    def return_object(self, obj):
        if(obj is None):
            return
        
        self.__pool.append(obj)

    def get_size(self) -> int:
        return len(self.__pool)