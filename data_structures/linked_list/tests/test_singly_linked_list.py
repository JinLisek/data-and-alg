import pytest

from data_structures.linked_list.singly_linked_list import (
    SinglyLinkedList,
    PeekOnEmptyLinkedList,
    DelOnEmptyLinkedList,
    AtOnEmptyLinkedList,
    NegativeIndex,
    OutOfRangeIndex,
)


@pytest.fixture(name="object_under_test")
def fix_object_under_test() -> SinglyLinkedList:
    return SinglyLinkedList()


def test_empty_list_has_size_of_zero(object_under_test: SinglyLinkedList):
    assert object_under_test.size() == 0


def test_after_single_insertion_has_size_of_one(
    object_under_test: SinglyLinkedList,
):
    object_under_test.insert_at_end(1)
    assert object_under_test.size() == 1


def test_after_multiple_insertions_has_matching_size(
    object_under_test: SinglyLinkedList,
):
    object_under_test.insert_at_end(8)
    object_under_test.insert_at_end(5)
    object_under_test.insert_at_end(7)

    assert object_under_test.size() == 3


def test_after_insertion_and_deletion_has_size_of_zero(
    object_under_test: SinglyLinkedList,
):
    object_under_test.insert_at_end(1)
    object_under_test.del_first()

    assert object_under_test.size() == 0


def test_head_returns_first_elem(
    object_under_test: SinglyLinkedList,
):
    first_elem = 133

    object_under_test.insert_at_end(elem=first_elem)
    object_under_test.insert_at_end(elem=96)

    head = object_under_test.head()

    assert head.data == first_elem


def test_given_one_elem_then_head_has_no_next(
    object_under_test: SinglyLinkedList,
):
    object_under_test.insert_at_end(elem=96)

    head = object_under_test.head()

    assert head.next is None


def test_given_two_elements_then_head_points_to_second(
    object_under_test: SinglyLinkedList,
):
    second_val = 78
    object_under_test.insert_at_end(elem=9)
    object_under_test.insert_at_end(elem=second_val)

    head = object_under_test.head()
    second_elem = head.next

    assert second_elem.data == second_val


def test_given_one_elem_then_at_zero_returns_that_elem(
    object_under_test: SinglyLinkedList,
):
    first_elem = 32
    object_under_test.insert_at_end(elem=first_elem)

    node = object_under_test.at(idx=0)
    assert node.data == first_elem


def test_given_one_elem_then_at_zero_has_no_next(
    object_under_test: SinglyLinkedList,
):
    object_under_test.insert_at_end(elem=43)

    node = object_under_test.at(idx=0)
    assert node.next is None


def test_given_two_elements_then_at_one_returns_second_elem(
    object_under_test: SinglyLinkedList,
):
    second_elem = 311
    object_under_test.insert_at_end(elem=78)
    object_under_test.insert_at_end(elem=second_elem)

    node = object_under_test.at(idx=1)
    assert node.data == second_elem


def test_del_on_empty_singly_linked_list_raises(object_under_test: SinglyLinkedList):
    with pytest.raises(DelOnEmptyLinkedList):
        object_under_test.del_first()


def test_head_on_empty_singly_linked_list_raises(object_under_test: SinglyLinkedList):
    with pytest.raises(PeekOnEmptyLinkedList):
        object_under_test.head()


def test_at_raises_when_list_is_empty(
    object_under_test: SinglyLinkedList,
):
    with pytest.raises(AtOnEmptyLinkedList):
        object_under_test.at(idx=6)


def test_at_raises_when_given_index_is_negative(
    object_under_test: SinglyLinkedList,
):
    object_under_test.insert_at_end(elem=18)
    negative_index = -1

    with pytest.raises(NegativeIndex) as exc:
        object_under_test.at(idx=negative_index)

    assert f"Given index: {negative_index} is negative" in str(exc.value)


def test_at_raises_when_given_index_equal_to_size(
    object_under_test: SinglyLinkedList,
):
    object_under_test.insert_at_end(elem=18)
    index_equal_to_size = 1

    with pytest.raises(OutOfRangeIndex) as exc:
        object_under_test.at(idx=index_equal_to_size)

    assert (
        f"Given index: {index_equal_to_size} is equal to or bigger than size: 1"
        in str(exc.value)
    )


def test_at_raises_when_given_index_bigger_than_size(
    object_under_test: SinglyLinkedList,
):
    object_under_test.insert_at_end(elem=18)
    index_equal_to_size = 7

    with pytest.raises(OutOfRangeIndex) as exc:
        object_under_test.at(idx=index_equal_to_size)

    assert (
        f"Given index: {index_equal_to_size} is equal to or bigger than size: 1"
        in str(exc.value)
    )
