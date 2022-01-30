from data_structures.binary_tree.exceptions import (
    MissingLeftChildOfNodeError,
    MissingRightChildOfNodeError,
)
from data_structures.binary_tree.node import ColorNode


def rotate_left(subtree_root: ColorNode) -> ColorNode:
    if subtree_root.right is None:
        raise MissingRightChildOfNodeError(f"Missing child of: {subtree_root.value}")

    new_root = subtree_root.right

    # if new_root.left is None:
    #     raise MissingLeftChildOfNodeError(f"Missing child of: {new_root.value}")

    left_child_of_new_root = new_root.left

    new_root.parent = subtree_root.parent
    new_root.left = subtree_root
    subtree_root.parent = new_root

    subtree_root.right = left_child_of_new_root
    if left_child_of_new_root is not None:
        left_child_of_new_root.parent = subtree_root

    return new_root


def rotate_right(subtree_root: ColorNode) -> ColorNode:
    if subtree_root.left is None:
        raise MissingLeftChildOfNodeError(f"Missing child of: {subtree_root.value}")

    new_root = subtree_root.left

    # if new_root.right is None:
    #     raise MissingRightChildOfNodeError(f"Missing child of: {new_root.value}")

    right_child_of_new_root = new_root.right

    new_root.parent = subtree_root.parent
    new_root.right = subtree_root
    subtree_root.parent = new_root

    subtree_root.left = right_child_of_new_root
    if right_child_of_new_root is not None:
        right_child_of_new_root.parent = subtree_root

    return new_root
