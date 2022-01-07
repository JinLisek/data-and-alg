from typing import List, Optional

from data_structures.binary_tree.node import Node
from data_structures.binary_tree.tree_traversers import traverse_tree_inorder


class DuplicatedValueInBSTError(RuntimeError):
    pass


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
                raise DuplicatedValueInBSTError(
                    f"Value {value} is already present in binary search tree"
                )

        current = Node(value=value, parent=previous)
        if current.value > previous.value:
            previous.right = current
        else:
            previous.left = current

    def traverse_inorder(self) -> List[int]:
        if self.is_empty():
            return []

        result: List[int] = []

        traverse_tree_inorder(node=self.__root, result=result)

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
