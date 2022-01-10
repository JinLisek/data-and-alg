import pytest
from data_structures.binary_tree.exceptions import (
    DuplicatedValueInTreeError,
    ValueNotFoundInTreeError,
)
from data_structures.binary_tree.red_black_tree import RedBlackTree


def test_given_empty_tree_then_is_empty_should_return_true():
    assert RedBlackTree().is_empty()


def test_given_empty_tree_then_is_empty_should_return_false():
    object_under_test = RedBlackTree()
    object_under_test.insert(15)

    assert not object_under_test.is_empty()


@pytest.mark.parametrize(
    "input_elements,expected_output",
    (
        ([], []),
        ([2, 4, 6, 8], [2, 4, 6, 8]),
        ([8, 6, 4, 2], [2, 4, 6, 8]),
        ([6, 4, 8, 2], [2, 4, 6, 8]),
    ),
)
def test_given_elements_then_traverse_inorder_should_return_them_in_order(
    input_elements, expected_output
):
    object_under_test = RedBlackTree()

    for ele in input_elements:
        object_under_test.insert(value=ele)

    assert expected_output == object_under_test.traverse_inorder()


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


def test_searching_for_a_value_which_node_is_not_a_leaf_should_return_node_pointing_to_other_node():
    object_under_test = RedBlackTree()
    object_under_test.insert(2)
    object_under_test.insert(8)

    result = object_under_test.search(2)

    assert result.right.value == 8


def test_deleting_only_node_should_leave_the_tree_empty():
    object_under_test = RedBlackTree()
    object_under_test.insert(22)

    object_under_test.delete(22)

    assert not object_under_test.traverse_preorder()


def test_deleting_right_leaf_should_cause_tree_to_lose_the_leaf():
    object_under_test = RedBlackTree()
    object_under_test.insert(44)
    object_under_test.insert(33)
    object_under_test.insert(55)

    object_under_test.delete(55)

    assert [44, 33] == object_under_test.traverse_preorder()


def test_deleting_left_leaf_should_cause_tree_to_lose_the_leaf():
    object_under_test = RedBlackTree()
    object_under_test.insert(44)
    object_under_test.insert(33)
    object_under_test.insert(55)

    object_under_test.delete(33)

    assert [44, 55] == object_under_test.traverse_preorder()


def test_deleting_node_with_only_right_child_should_replace_the_node_with_the_only_child():
    object_under_test = RedBlackTree()
    object_under_test.insert(33)
    object_under_test.insert(44)
    object_under_test.insert(55)

    object_under_test.delete(44)

    assert [33, 55] == object_under_test.traverse_preorder()


def test_deleting_node_with_only_left_child_hould_replace_the_node_with_the_only_child():
    object_under_test = RedBlackTree()
    object_under_test.insert(55)
    object_under_test.insert(44)
    object_under_test.insert(33)

    object_under_test.delete(44)

    assert [55, 33] == object_under_test.traverse_preorder()


def test_deleting_node_with_two_children_should_replace_the_node_with_successor():
    object_under_test = RedBlackTree()
    object_under_test.insert(44)
    object_under_test.insert(33)
    object_under_test.insert(55)

    object_under_test.delete(44)

    assert [55, 33] == object_under_test.traverse_preorder()


def test_deleting_nonexistent_value_should_raise():
    object_under_test = RedBlackTree()
    object_under_test.insert(44)

    nonexistent_value = 22

    with pytest.raises(ValueNotFoundInTreeError) as err:
        object_under_test.delete(nonexistent_value)

    assert f"{nonexistent_value}" in str(err)
