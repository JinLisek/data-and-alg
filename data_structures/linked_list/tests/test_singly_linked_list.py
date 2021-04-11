import pytest

from data_structures.linked_list.singly_linked_list import (
    SinglyLinkedList,
    PeekOnEmptyLinkedList,
    DelOnEmptyLinkedList,
)


@pytest.fixture(name="object_under_test")
def fix_object_under_test() -> SinglyLinkedList:
    return SinglyLinkedList()


def test_empty_singly_linked_list_has_size_of_zero(object_under_test: SinglyLinkedList):
    assert object_under_test.size() == 0


def test_singly_linked_list_after_addition_has_size_of_one(
    object_under_test: SinglyLinkedList,
):
    object_under_test.insert_at_start(1)
    assert object_under_test.size() == 1


def test_singly_linked_list_after_multiple_additions_has_matching_size(
    object_under_test: SinglyLinkedList,
):
    object_under_test.insert_at_start(8)
    object_under_test.insert_at_start(5)
    object_under_test.insert_at_start(7)
    assert object_under_test.size() == 3


def test_singly_linked_list_after_add_and_del_has_size_of_zero(
    object_under_test: SinglyLinkedList,
):
    object_under_test.insert_at_start(1)
    object_under_test.del_first()
    assert object_under_test.size() == 0


def test_del_on_empty_singly_linked_list_raises(object_under_test: SinglyLinkedList):
    with pytest.raises(DelOnEmptyLinkedList):
        object_under_test.del_first()


def test_head_on_empty_singly_linked_list_raises(object_under_test: SinglyLinkedList):
    with pytest.raises(PeekOnEmptyLinkedList):
        object_under_test.head()


def test_head_returns_node_with_inserted_value(object_under_test: SinglyLinkedList):
    expected_value = 89
    object_under_test.insert_at_start(elem=expected_value)
    head = object_under_test.head()
    assert head.data == expected_value


def test_head_returns_second_node_inserted_by_insert_at_start(
    object_under_test: SinglyLinkedList,
):
    expected_value = 133

    object_under_test.insert_at_start(elem=96)
    object_under_test.insert_at_start(elem=expected_value)

    head = object_under_test.head()

    assert head.data == expected_value
