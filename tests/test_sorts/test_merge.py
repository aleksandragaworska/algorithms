import pytest

from sorts.merge.merge import (
    merge_sort
)

from tests.test_sorts.conftest import test_cases


@pytest.mark.parametrize('not_sorted, expected', test_cases)
def test_merge_sort(not_sorted, expected):
    assert merge_sort(not_sorted) == expected
