import pytest

from graph_searches.dijkstra import dijkstra

from tests.test_graphs.conftest import test_graph_weighted_distance_cases, graph_weighted_directed


@pytest.mark.parametrize('v_from, v_to, expected', test_graph_weighted_distance_cases)
def test_dijkstra(v_from, v_to, expected):
    assert dijkstra(v_from, v_to, graph_weighted_directed) == expected
