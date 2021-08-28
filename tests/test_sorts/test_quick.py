import pytest

from sorts.quick.quick import (
    quick_sort
)

from tests.test_sorts.conftest import test_cases


@pytest.mark.parametrize('not_sorted, expected', test_cases)
def test_quick_sort(not_sorted, expected):
    assert quick_sort(not_sorted) == expected
