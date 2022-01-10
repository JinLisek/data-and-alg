import pytest
from data_structures.binary_tree.exceptions import (
    MissingLeftChildOfNodeError,
    MissingRightChildOfNodeError,
)
from data_structures.binary_tree.node import Node
from data_structures.binary_tree.tree_rotations import rotate_left


def test_rotate_left_should_raise_an_error_when_subtree_root_has_no_right_child():
    root_value = 33

    with pytest.raises(MissingRightChildOfNodeError) as err:
        rotate_left(subtree_root=Node(value=root_value))

    assert f"{root_value}" in str(err)


def test_rotate_left_should_rainse_an_error_when_new_root_has_no_left_child():
    new_root_value = 22
    new_root = Node(value=new_root_value)

    with pytest.raises(MissingLeftChildOfNodeError) as err:
        rotate_left(subtree_root=Node(value=33, right=new_root))

    assert f"{new_root_value}" in str(err)


def test_rotate_left_should_not_change_left_child_of_previous_root():
    left_child_of_previous_root = Node(value=0)
    new_root = Node(value=3, left=Node(value=77))
    previous_root = Node(value=1, left=left_child_of_previous_root, right=new_root)

    rotate_left(subtree_root=previous_root)

    assert previous_root.left is left_child_of_previous_root


def test_rotate_left_should_not_change_right_child_of_new_root():
    right_child_of_new_root = Node(value=3)
    new_root = Node(value=2, left=Node(value=88), right=right_child_of_new_root)
    previous_root = Node(value=1, right=new_root)

    rotate_left(subtree_root=previous_root)

    assert new_root.right is right_child_of_new_root


def test_rotate_left_should_make_previous_root_a_left_child_to_new_root():
    new_root = Node(value=2, left=Node(value=99))
    previous_root = Node(value=1, right=new_root)

    rotate_left(subtree_root=previous_root)

    assert new_root.left is previous_root


def test_rotate_left_should_make_new_root_right_child_a_left_child_to_previous_root():
    left_child_of_new_root = Node(value=2)
    new_root = Node(value=3, left=left_child_of_new_root)
    previous_root = Node(value=2, right=new_root)

    rotate_left(subtree_root=previous_root)

    assert previous_root.right is left_child_of_new_root
