from typing import List


def swap(collection: List[int], idx1: int, idx2: int) -> None:
    collection[idx1], collection[idx2] = collection[idx2], collection[idx1]


def quick_sort(collection: List[int]) -> List[int]:
    def inner(collection: List[int], left_idx: int, right_idx: int):
        if left_idx >= right_idx:
            return

        pivot = right_idx
        smaller_search_index = right_idx - 1
        bigger_search_index = left_idx

        while bigger_search_index < smaller_search_index:
            while (
                collection[bigger_search_index] < collection[pivot]
                and bigger_search_index < pivot
            ):
                bigger_search_index += 1

            while (
                collection[smaller_search_index] >= collection[pivot]
                and smaller_search_index > left_idx
            ):
                smaller_search_index -= 1

            if bigger_search_index < smaller_search_index:
                swap(collection, bigger_search_index, smaller_search_index)

        if collection[bigger_search_index] > collection[pivot]:
            swap(collection, pivot, bigger_search_index)

        inner(
            collection=collection, left_idx=left_idx, right_idx=bigger_search_index - 1
        )

        inner(
            collection=collection,
            left_idx=bigger_search_index + 1,
            right_idx=right_idx,
        )

    if len(collection) < 2:
        return collection

    inner(collection=collection, left_idx=0, right_idx=len(collection) - 1)

    return collection


def main():
    quick_sort(collection=[])


if __name__ == "__main__":
    main()
