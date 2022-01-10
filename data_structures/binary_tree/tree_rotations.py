from data_structures.binary_tree.exceptions import (
    MissingLeftChildOfNodeError,
    MissingRightChildOfNodeError,
)
from data_structures.binary_tree.node import Node


def rotate_left(subtree_root: Node) -> None:
    if subtree_root.right is None:
        raise MissingRightChildOfNodeError(
            f"Missing right child of: {subtree_root.value}"
        )

    new_root = subtree_root.right

    if new_root.left is None:
        raise MissingLeftChildOfNodeError(f"Missing left child of: {new_root.value}")

    left_child_of_new_root = new_root.left
    new_root.left = subtree_root
    subtree_root.right = left_child_of_new_root
