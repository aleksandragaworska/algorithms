import pytest

from searches.binary_search import (
    existed_binary_search,
    idx_binary_search,
)

from tests.test_searches.conftest import (
    test_cases_exist,
    test_cases_idx,
)


@pytest.mark.parametrize('search_list, searched_number, expected', test_cases_exist)
def test_binary_search_number_existed(search_list, searched_number, expected):
    assert existed_binary_search(search_list, searched_number) is expected


@pytest.mark.parametrize('search_list, searched_number, expected', test_cases_idx)
def test_binary_seatch_idx(search_list, searched_number, expected):
    assert idx_binary_search(search_list, searched_number) == expected
