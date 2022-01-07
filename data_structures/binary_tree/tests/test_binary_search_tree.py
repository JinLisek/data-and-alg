import pytest
from data_structures.binary_tree.binary_search_tree import (
    BinarySearchTree,
    DuplicatedValueInBSTError,
)


def test_given_empty_tree_then_is_empty_should_return_true():
    assert BinarySearchTree().is_empty()


def test_given_empty_tree_then_is_empty_should_return_false():
    object_under_test = BinarySearchTree()
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
    object_under_test = BinarySearchTree()

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
    object_under_test = BinarySearchTree()

    for ele in input_elements:
        object_under_test.insert(value=ele)

    assert expected_output == object_under_test.traverse_preorder()


def test_inserting_duplicated_value_should_raise_an_error():
    object_under_test = BinarySearchTree()

    duplicated_elem = 8
    object_under_test.insert(duplicated_elem)

    with pytest.raises(DuplicatedValueInBSTError) as err:
        object_under_test.insert(duplicated_elem)

    assert f"{duplicated_elem}" in str(err)


def test_search_on_empty_tree_returns_none():
    object_under_test = BinarySearchTree()

    assert object_under_test.search(8) is None


def test_search_on_a_tree_containing_given_value_should_return_node_with_the_value():
    object_under_test = BinarySearchTree()
    object_under_test.insert(8)

    result = object_under_test.search(8)

    assert result.value == 8


def test_searching_for_a_value_which_node_is_not_a_leaf_should_return_node_pointing_to_other_node():
    object_under_test = BinarySearchTree()
    object_under_test.insert(2)
    object_under_test.insert(8)

    result = object_under_test.search(2)

    assert result.right.value == 8
