from typing import List, Optional

from data_structures.binary_tree.exceptions import (
    DuplicatedValueInTreeError,
    ValueNotFoundInTreeError,
)
from data_structures.binary_tree.node import ColorNode, Node
from data_structures.binary_tree.tree_rotations import rotate_left, rotate_right
from data_structures.binary_tree.tree_traversers import (
    traverse_tree_inorder,
    traverse_tree_preorder,
)


def get_min_node(node: Node) -> Node:
    while node.left is not None:
        node = node.left
    return node


class RedBlackTree:
    def __init__(self) -> None:
        self.__root: Optional[ColorNode] = None

    def is_empty(self) -> bool:
        return self.__root is None

    def get_root(self) -> Optional[ColorNode]:
        return self.__root

    def insert(self, value: int) -> None:
        if self.is_empty():
            # Case_I3: N is the root and red
            self.__root = ColorNode(value=value, is_red=False)
            return

        current: Optional[ColorNode] = self.__root

        while current is not None:
            if value == current.value:
                raise DuplicatedValueInTreeError(f"Value {value} is already present")

            previous = current
            current = current.left if value < current.value else current.right

        current = ColorNode(value=value, is_red=True, parent=previous)
        if current.value > previous.value:
            previous.right = current
        else:
            previous.left = current

        if not current.parent.is_red:
            # Case_I1 (P is black)
            return

        if current.parent.parent is None:
            # Case_I4
            current.parent.is_red = False
            return

        if current.is_uncle_black():
            # Case_I6
            if current is current.parent.right:
                new_subtree_root = rotate_left(subtree_root=current.parent.parent)
                new_subtree_root.is_red = False
                new_subtree_root.left.is_red = True
            else:
                new_subtree_root = rotate_right(subtree_root=current.parent.parent)
                new_subtree_root.is_red = False
                new_subtree_root.right.is_red = True
            if new_subtree_root.parent is None:
                self.__root = new_subtree_root
            # current = current.parent

        # print(f"calling rotate_left root: {self.get_root()}")
        # current = rotate_left(subtree_root=previous.parent)
        # print(f"AFTER rotate_left root: {self.get_root()}")

    def delete(self, value: int) -> None:
        current = self.__root

        while current is not None and current.value != value:
            parent = current
            current = current.left if value < current.value else current.right

        if current is None:
            raise ValueNotFoundInTreeError(f"Value {value} not found")

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

    def search(self, value: int) -> Optional[ColorNode]:
        current = self.__root

        while current is not None and current.value != value:
            current = current.left if value < current.value else current.right

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
    tree = RedBlackTree()
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
