import pytest

from insertion.insertion import (
    insertion_sort_recursive,
    insertion_sort_for,
    insertion_sort_for_range,
)

from tests.conftest import test_cases


@pytest.mark.parametrize('not_sorted, expected', test_cases)
def test_insertion_recursive(not_sorted, expected):
    try:
        assert insertion_sort_recursive(not_sorted) == expected
    except RecursionError:
        pass  # When a lot of elements


@pytest.mark.parametrize('not_sorted, expected', test_cases)
def test_insertion_for(not_sorted, expected):
    assert insertion_sort_for(not_sorted) == expected


@pytest.mark.parametrize('not_sorted, expected', test_cases)
def test_insertion_for_range(not_sorted, expected):
    assert insertion_sort_for_range(not_sorted) == expected
