from typing import List, Optional

from data_structures.binary_tree.node import Node
from data_structures.binary_tree.tree_traversers import (
    traverse_tree_inorder,
    traverse_tree_preorder,
)


class DuplicatedValueInBSTError(RuntimeError):
    pass


class ValueNotFoundInBSTError(RuntimeError):
    pass


def get_min_node(node: Node) -> Node:
    while node.left is not None:
        node = node.left
    return node


class BinarySearchTree:
    def __init__(self) -> None:
        self.__root: Optional[Node] = None

    def is_empty(self) -> bool:
        return self.__root is None

    def insert(self, value: int) -> None:
        if self.is_empty():
            self.__root = Node(value=value)
            return

        current: Optional[Node] = self.__root

        while current is not None:
            previous = current
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                raise DuplicatedValueInBSTError(f"Value {value} is already present")

        current = Node(value=value)
        if current.value > previous.value:
            previous.right = current
        else:
            previous.left = current

    def delete(self, value: int) -> None:
        current = self.__root

        while current is not None and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current is None:
            raise ValueNotFoundInBSTError(f"Value {value} not found")

        if current.left is None and current.right is None:
            if current is self.__root:
                self.__root = None
                return

            if parent.right is current:
                parent.right = None
            else:
                parent.left = None
        elif current.left is not None and current.right is not None:
            successor_value = get_min_node(node=current.right).value
            self.delete(value=successor_value)
            current.value = successor_value
        else:
            child = current.left if current.left is not None else current.right

            if parent.right is current:
                parent.right = child
            else:
                parent.left = child

    def search(self, value: int) -> Optional[Node]:
        current = self.__root

        while current is not None and current.value != value:
            if value < current.value:
                current = current.left
            else:
                current = current.right

        return current

    def traverse_inorder(self) -> List[int]:
        if self.is_empty():
            return []

        result: List[int] = []

        traverse_tree_inorder(node=self.__root, result=result)

        return result

    def traverse_preorder(self) -> List[int]:
        if self.is_empty():
            return []

        result: List[int] = []

        traverse_tree_preorder(node=self.__root, result=result)

        return result


def main():
    tree = BinarySearchTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)

    print(tree.traverse_inorder())


if __name__ == "__main__":
    main()
