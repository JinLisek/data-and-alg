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
        if self.__size < 1:
            raise DelOnEmptyLinkedList

        self.__size -= 1

    def head(self) -> LinkedListNode[T]:
        if self.__size < 1:
            raise PeekOnEmptyLinkedList

        return self.__head

    def size(self) -> int:
        return self.__size


class PeekOnEmptyLinkedList(Exception):
    pass


class DelOnEmptyLinkedList(Exception):
    pass
