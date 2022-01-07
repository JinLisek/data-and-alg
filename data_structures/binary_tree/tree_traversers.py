from typing import List, Optional

from data_structures.binary_tree.node import Node


def traverse_tree_inorder(node: Optional[Node], result: List[int]) -> None:
    if node is None:
        return

    traverse_tree_inorder(node.left, result)
    result.append(node.value)
    traverse_tree_inorder(node.right, result)


def traverse_tree_preorder(node: Optional[Node], result: List[int]) -> None:
    if node is None:
        return

    result.append(node.value)
    traverse_tree_preorder(node.left, result)
    traverse_tree_preorder(node.right, result)
