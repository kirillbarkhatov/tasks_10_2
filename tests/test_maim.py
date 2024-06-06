import pytest

from src.main import calculate_taxes

def test_calculate_taxes():
    assert calculate_taxes([1.0, 2.0], 10) == [1.1, 2.2]

    with pytest.raises(ValueError):
        calculate_taxes([1.0, 2.0], -10)

    with pytest.raises(ValueError):
        calculate_taxes([-11.0, 2.0], 10)