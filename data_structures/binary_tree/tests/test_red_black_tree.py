import pytest
from data_structures.binary_tree.exceptions import (
    DuplicatedValueInTreeError,
    ValueNotFoundInTreeError,
)
from data_structures.binary_tree.red_black_tree import RedBlackTree


def test_given_empty_tree_then_is_empty_should_return_true():
    assert RedBlackTree().is_empty()


def test_given_one_node_then_is_empty_should_return_false():
    object_under_test = RedBlackTree()
    object_under_test.insert(15)

    assert not object_under_test.is_empty()


def test_inserting_root_and_two_children_then_root_value_should_be_in_the_middle():
    object_under_test = RedBlackTree()
    object_under_test.insert(2)
    object_under_test.insert(1)
    object_under_test.insert(3)

    assert object_under_test.get_root().value == 2


def test_inserting_root_and_two_children_then_left_child_value_should_be_lowest():
    object_under_test = RedBlackTree()
    object_under_test.insert(15)
    object_under_test.insert(8)
    object_under_test.insert(33)

    assert object_under_test.get_root().left.value == 8


def test_inserting_root_and_two_children_then_right_child_value_should_be_highest():
    object_under_test = RedBlackTree()
    object_under_test.insert(15)
    object_under_test.insert(8)
    object_under_test.insert(33)

    assert object_under_test.get_root().right.value == 33


def test_inserting_root_and_two_children_then_root_should_be_black():
    object_under_test = RedBlackTree()
    object_under_test.insert(15)
    object_under_test.insert(8)
    object_under_test.insert(33)

    assert object_under_test.get_root().is_red is False


def test_inserting_root_and_two_children_then_left_child_should_be_red():
    object_under_test = RedBlackTree()
    object_under_test.insert(15)
    object_under_test.insert(8)
    object_under_test.insert(33)

    assert object_under_test.get_root().left.is_red is True


def test_inserting_root_and_two_children_then_right_child_should_be_red():
    object_under_test = RedBlackTree()
    object_under_test.insert(15)
    object_under_test.insert(8)
    object_under_test.insert(33)

    assert object_under_test.get_root().right.is_red is True


def test_inserting_three_nodes_in_ascending_line_then_root_value_should_be_in_the_middle():
    object_under_test = RedBlackTree()
    object_under_test.insert(1)
    object_under_test.insert(2)
    object_under_test.insert(3)

    assert object_under_test.get_root().value == 2


def test_inserting_three_nodes_in_ascending_line_then_left_child_value_should_be_lowest():
    object_under_test = RedBlackTree()
    object_under_test.insert(1)
    object_under_test.insert(2)
    object_under_test.insert(3)

    assert object_under_test.get_root().left.value == 1


def test_inserting_three_nodes_in_ascending_line_then_right_child_value_should_be_highest():
    object_under_test = RedBlackTree()
    object_under_test.insert(1)
    object_under_test.insert(2)
    object_under_test.insert(3)

    assert object_under_test.get_root().right.value == 3


def test_inserting_three_nodes_in_ascending_line_then_root_should_be_black():
    object_under_test = RedBlackTree()
    object_under_test.insert(1)
    object_under_test.insert(2)
    object_under_test.insert(3)

    assert object_under_test.get_root().is_red is False


def test_inserting_three_nodes_in_ascending_line_then_left_child_should_be_red():
    object_under_test = RedBlackTree()
    object_under_test.insert(1)
    object_under_test.insert(2)
    object_under_test.insert(3)

    assert object_under_test.get_root().left.is_red is True


def test_inserting_three_nodes_in_ascending_line_then_right_child_should_be_red():
    object_under_test = RedBlackTree()
    object_under_test.insert(1)
    object_under_test.insert(2)
    object_under_test.insert(3)

    assert object_under_test.get_root().right.is_red is True


def test_inserting_three_nodes_in_descending_line_then_root_value_should_be_in_the_middle():
    object_under_test = RedBlackTree()
    object_under_test.insert(3)
    object_under_test.insert(2)
    object_under_test.insert(1)

    assert object_under_test.get_root().value == 2


def test_inserting_three_nodes_in_descending_line_then_left_child_value_should_be_lowest():
    object_under_test = RedBlackTree()
    object_under_test.insert(3)
    object_under_test.insert(2)
    object_under_test.insert(1)

    assert object_under_test.get_root().left.value == 1


def test_inserting_three_nodes_in_descending_line_then_right_child_value_should_be_highest():
    object_under_test = RedBlackTree()
    object_under_test.insert(3)
    object_under_test.insert(2)
    object_under_test.insert(1)

    assert object_under_test.get_root().right.value == 3


def test_inserting_three_nodes_in_descending_line_then_root_should_be_black():
    object_under_test = RedBlackTree()
    object_under_test.insert(3)
    object_under_test.insert(2)
    object_under_test.insert(1)

    assert object_under_test.get_root().is_red is False


def test_inserting_three_nodes_in_descending_line_then_left_child_should_be_red():
    object_under_test = RedBlackTree()
    object_under_test.insert(3)
    object_under_test.insert(2)
    object_under_test.insert(1)

    assert object_under_test.get_root().left.is_red is True


def test_inserting_three_nodes_in_descending_line_then_right_child_should_be_red():
    object_under_test = RedBlackTree()
    object_under_test.insert(3)
    object_under_test.insert(2)
    object_under_test.insert(1)

    assert object_under_test.get_root().right.is_red is True


@pytest.mark.parametrize(
    "input_elements,expected_output",
    (([], []),),
)
def test_given_elements_then_traverse_inorder_should_return_them_in_order(
    input_elements, expected_output
):
    object_under_test = RedBlackTree()

    for ele in input_elements:
        object_under_test.insert(value=ele)

    assert expected_output == object_under_test.traverse_inorder()


@pytest.mark.skip(reason="RedBlackTree not implemented yet")
@pytest.mark.parametrize(
    "input_elements,expected_output",
    (
        ([], []),
        ([2, 4, 6, 8], [2, 4, 6, 8]),
        ([8, 6, 4, 2], [8, 6, 4, 2]),
        ([6, 4, 8, 2], [6, 4, 2, 8]),
    ),
)
def test_given_elements_then_traverse_preorder_should_return_elements_in_preorder_with_parents_first(
    input_elements, expected_output
):
    object_under_test = RedBlackTree()

    for ele in input_elements:
        object_under_test.insert(value=ele)

    assert expected_output == object_under_test.traverse_preorder()


def test_inserting_duplicated_value_should_raise_an_error():
    object_under_test = RedBlackTree()

    duplicated_elem = 8
    object_under_test.insert(duplicated_elem)

    with pytest.raises(DuplicatedValueInTreeError) as err:
        object_under_test.insert(duplicated_elem)

    assert f"{duplicated_elem}" in str(err)


def test_search_on_empty_tree_returns_none():
    object_under_test = RedBlackTree()

    assert object_under_test.search(8) is None


def test_search_on_a_tree_containing_given_value_should_return_node_with_the_value():
    object_under_test = RedBlackTree()
    object_under_test.insert(8)

    result = object_under_test.search(8)

    assert result.value == 8


def test_deleting_only_node_should_leave_the_tree_empty():
    object_under_test = RedBlackTree()
    object_under_test.insert(22)

    object_under_test.delete(22)

    assert not object_under_test.traverse_preorder()


def test_deleting_nonexistent_value_should_raise():
    object_under_test = RedBlackTree()
    object_under_test.insert(44)

    nonexistent_value = 22

    with pytest.raises(ValueNotFoundInTreeError) as err:
        object_under_test.delete(nonexistent_value)

    assert f"{nonexistent_value}" in str(err)
