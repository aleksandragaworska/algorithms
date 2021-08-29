import pytest

from graph_searches.dfs import dfs, dfs_while

from tests.test_graphs.conftest import test_graph_cases, graph_directed


@pytest.mark.parametrize('v_from, v_to, expected', test_graph_cases)
def test_dfs(v_from, v_to, expected):
    assert dfs(v_from, v_to, graph_directed) is expected


@pytest.mark.parametrize('v_from, v_to, expected', test_graph_cases)
def test_dfs_while(v_from, v_to, expected):
    assert dfs_while(v_from, v_to, graph_directed) is expected
