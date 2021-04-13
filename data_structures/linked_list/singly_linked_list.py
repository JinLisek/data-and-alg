from typing import Optional


class LinkedListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Optional[LinkedListNode] = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.__size = 0
        self.__head: Optional[LinkedListNode] = None

    def insert_at_end(self, elem) -> None:
        new_elem = LinkedListNode(data=elem)

        if self.__head is None:
            self.__head = new_elem
        else:
            last_node = self.__head

            while last_node.next is not None:
                last_node = last_node.next

            last_node.next = new_elem

        self.__size += 1

    def del_first(self) -> None:
        if self.is_empty():
            raise DelOnEmptyLinkedList

        self.__size -= 1

    def head(self):
        if self.is_empty():
            raise PeekOnEmptyLinkedList

        return self.__head

    def at(self, idx):
        if self.is_empty():
            raise AtOnEmptyLinkedList()

        if idx < 0:
            raise NegativeIndex(f"Given index: {idx} is negative!")

        if idx >= self.size():
            raise OutOfRangeIndex(
                f"Given index: {idx} is equal to or bigger than size: {self.size()}"
            )

        elem = self.__head
        for _ in range(0, idx):
            elem = elem.next

        return elem

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


class ElementHasNoNext(Exception):
    pass
