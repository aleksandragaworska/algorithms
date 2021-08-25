import pytest

from bubble.bubble import (
    bubble_sort
)

from tests.conftest import test_cases


@pytest.mark.parametrize('not_sorted, expected', test_cases)
def test_bubble_sort(not_sorted, expected):
    assert bubble_sort(not_sorted) == expected
