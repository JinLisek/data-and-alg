import pytest
from quick_sort.quick_sort import quick_sort


@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([2, 1], [1, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([8, 6, 7, 5, 2, 4], [2, 4, 5, 6, 7, 8]),
    ],
)
def test_given_list_should_return_sorted_copy(input_list, expected_output):
    assert quick_sort(collection=input_list) == expected_output
