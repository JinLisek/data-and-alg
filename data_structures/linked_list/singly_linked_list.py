from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class LinkedListNode(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.next: Optional[LinkedListNode[T]] = None


class NullLinkedListNode(LinkedListNode):
    def __init__(self) -> None:
        super().__init__(data=None)


class SinglyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.__size = 0
        self.__head: LinkedListNode[T] = NullLinkedListNode()

    def insert_at_start(self, elem: T) -> None:
        new_head = LinkedListNode(data=elem)

        if self.__head is NullLinkedListNode:
            self.__head = new_head
        else:
            new_head.next = self.__head
            self.__head = new_head

        self.__size += 1

    def del_first(self) -> None:
        if self.is_empty():
            raise DelOnEmptyLinkedList

        self.__size -= 1

    def head(self) -> LinkedListNode[T]:
        if self.is_empty():
            raise PeekOnEmptyLinkedList

        return self.__head

    def at(self, idx: int) -> LinkedListNode[T]:
        if self.is_empty():
            raise AtOnEmptyLinkedList()

        if idx < 0:
            raise NegativeIndex(f"Given index: {idx} is negative!")

        if idx >= self.size():
            raise OutOfRangeIndex(
                f"Given index: {idx} is equal to or bigger than size: {self.size()}"
            )

        return self.__head

    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return self.size() < 1


class PeekOnEmptyLinkedList(Exception):
    pass


class DelOnEmptyLinkedList(Exception):
    pass


class AtOnEmptyLinkedList(Exception):
    pass


class NegativeIndex(Exception):
    pass


class OutOfRangeIndex(Exception):
    pass
