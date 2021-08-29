import pytest

from graph_searches.bfs import bfs, bfs_distance

from tests.test_graphs.conftest import test_graph_cases, graph_directed, test_graph_distance_cases


@pytest.mark.parametrize('v_from, v_to, expected', test_graph_cases)
def test_bfs(v_from, v_to, expected):
    assert bfs(v_from, v_to, graph_directed) is expected


@pytest.mark.parametrize('v_from, v_to, expected', test_graph_distance_cases)
def test_bfs_distance(v_from, v_to, expected):
    assert bfs_distance(v_from, v_to, graph_directed) == expected
