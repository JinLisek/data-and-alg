from typing import TypeVar, Generic

T = TypeVar("T")


class Queue(Generic[T]):
    def enqueue(self, val: T):
        pass

    def deque(self) -> T:
        pass
