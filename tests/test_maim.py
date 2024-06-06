import pytest

from src.main import calculate_taxes, calculate_tax

def test_calculate_taxes():
    assert calculate_taxes([1.0, 2.0], 10) == [1.1, 2.2]

    with pytest.raises(ValueError):
        calculate_taxes([1.0, 2.0], -10)

    with pytest.raises(ValueError):
        calculate_taxes([-11.0, 2.0], 10)


def test_calculate_tax():
    result = calculate_tax(100, 10)
    assert result == 110.0

    result = calculate_tax(50, 5)
    assert result == 52.5

    with pytest.raises(ValueError):
        calculate_tax(1, -10)

    with pytest.raises(ValueError):
        calculate_tax(-11.0, 10)