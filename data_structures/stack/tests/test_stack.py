import pytest

from data_structures.stack.stack import Stack, PopFromEmptyStack


@pytest.fixture(name="object_under_test")
def fix_object_under_test() -> Stack:
    return Stack()


def test_new_stack_should_be_empty(object_under_test):
    assert object_under_test.is_empty()


def test_stack_should_be_empty_after_push_and_pop(object_under_test):
    object_under_test.push(7)
    object_under_test.pop()

    assert object_under_test.is_empty()


def test_stack_should_not_be_empty_after_push(object_under_test):
    object_under_test.push(7)

    assert not object_under_test.is_empty()


def test_new_stack_should_have_size_zero(object_under_test):
    assert object_under_test.size() == 0


def test_stack_should_have_size_zero_after_push_and_pop(object_under_test):
    object_under_test.push(7)
    object_under_test.pop()

    assert object_under_test.size() == 0


def test_stack_size_should_match_number_of_pushes(object_under_test):
    object_under_test.push(7)
    object_under_test.push(5)

    assert object_under_test.size() == 2


def test_pop_gives_pushed_value(object_under_test):
    expected_value = 4

    object_under_test.push(val=expected_value)

    assert expected_value == object_under_test.pop()


def test_raises_when_popped_without_anything_in_stack(object_under_test):
    with pytest.raises(PopFromEmptyStack):
        object_under_test.pop()
