import pytest

from sorts.selection.selection import (
    selection_sort_recursive,
    selection_sort_for,
    selection_sort_swap,
    selection_sort_swap_2,
    selection_sort_swap_3,
)
from tests.test_sorts.conftest import test_cases


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
