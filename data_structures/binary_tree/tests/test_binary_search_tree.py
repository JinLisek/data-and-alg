import pytest
from data_structures.binary_tree.binary_search_tree import (
    BinarySearchTree,
    DuplicatedValueInBSTError,
)


def test_given_empty_tree_then_is_empty_should_return_true():
    assert BinarySearchTree().is_empty()


def test_given_empty_tree_then_is_empty_should_return_false():
    tree = BinarySearchTree()
    tree.insert(15)

    assert not tree.is_empty()


@pytest.mark.parametrize(
    "input_elements,expected_output",
    (
        ([], []),
        ([2, 4, 6, 8], [2, 4, 6, 8]),
        ([8, 6, 4, 2], [2, 4, 6, 8]),
        ([6, 4, 8, 2], [2, 4, 6, 8]),
    ),
)
def test_given_elements_then_traverse_indorder_should_return_them_in_order(
    input_elements, expected_output
):
    tree = BinarySearchTree()

    for ele in input_elements:
        tree.insert(value=ele)

    assert expected_output == tree.traverse_inorder()


def test_inserting_duplicated_value_should_raise_an_error():
    tree = BinarySearchTree()

    duplicated_elem = 8
    tree.insert(duplicated_elem)

    with pytest.raises(DuplicatedValueInBSTError) as err:
        tree.insert(duplicated_elem)

    assert f"{duplicated_elem}" in str(err)


def test_search_on_empty_tree_returns_none():
    tree = BinarySearchTree()

    assert tree.search(8) is None


def test_search_on_a_tree_containing_given_value_should_return_node_with_the_value():
    tree = BinarySearchTree()
    tree.insert(8)

    result = tree.search(8)

    assert result.value == 8


def test_searching_for_a_value_which_node_is_not_a_leaf_should_return_node_pointing_to_other_node():
    tree = BinarySearchTree()
    tree.insert(2)
    tree.insert(8)

    result = tree.search(2)

    assert result.right.value == 8
