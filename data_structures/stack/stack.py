from typing import List, TypeVar, Generic

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.__data: List[T] = []

    def pop(self) -> T:
        if self.is_empty():
            raise PopFromEmptyStack

        return self.__data.pop()

    def push(self, val: T) -> None:
        self.__data.append(val)

    def is_empty(self) -> bool:
        return self.size() < 1

    def size(self) -> int:
        return len(self.__data)


class PopFromEmptyStack(Exception):
    pass
