import pytest

from others.fibonacci import fibonacci_sequence

from tests.test_others.conftest import test_fibonacci_cases


@pytest.mark.parametrize('n, expected_number', test_fibonacci_cases)
def test_fibonacci_sequence(n, expected_number):
    assert fibonacci_sequence(n) == expected_number
