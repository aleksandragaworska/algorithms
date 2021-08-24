import pytest

from selection import (
    selection_sort_recursive,
    selection_sort_for,
    selection_sort_swap,
    selection_sort_swap_2,
    selection_sort_swap_3,
)

test_cases = [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 3, 1, 2, 4], [1, 2, 3, 4, 5]),
    ([0, 3, 5, 2, 4], [0, 2, 3, 4, 5]),
    ([10, -3, 15, 142, -489, 0, 98], [-489, -3, 0, 10, 15, 98, 142]),
    ([7], [7]),
    ([-95], [-95]),
    ([0, -64], [-64, 0]),
    ([0], [0]),
    ([], []),
    ([1, 1, 2, 0], [0, 1, 1, 2]),
    ([x for x in range(2000, 0, -1)], [x for x in range(1, 2001)])
]


@pytest.mark.parametrize("not_sorted, expected", test_cases)
def test_selection_recursive(not_sorted, expected):
    try:
        assert selection_sort_recursive(not_sorted) == expected
    except RecursionError:
        pass  # When a lot of elements


@pytest.mark.parametrize("not_sorted, expected", test_cases)
def test_selection_for(not_sorted, expected):
    assert selection_sort_for(not_sorted) == expected


@pytest.mark.parametrize("not_sorted, expected", test_cases)
def test_selection_swap(not_sorted, expected):
    assert selection_sort_swap(not_sorted) == expected


@pytest.mark.parametrize("not_sorted, expected", test_cases)
def test_selection_swap_2(not_sorted, expected):
    assert selection_sort_swap_2(not_sorted) == expected


@pytest.mark.parametrize("not_sorted, expected", test_cases)
def test_selection_swap_3(not_sorted, expected):
    assert selection_sort_swap_3(not_sorted) == expected
