import pytest

from data_structures.queue.queue import Queue


@pytest.fixture(name="object_under_test")
def fix_object_under_test() -> Queue:
    return Queue()


def test_enqueue(object_under_test: Queue):
    object_under_test.enqueue(4)


def test_deque(object_under_test: Queue):
    object_under_test.deque()
