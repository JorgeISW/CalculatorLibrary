import pytest
from CalculatorLibrary import calculator


def test_add() -> None:
    assert calculator.add(1, 2) == (1 + 2)


def test_add_value_error() -> None:
    with pytest.raises(TypeError):
        calculator.add(1, "2")


def test_subtract() -> None:
    assert calculator.subtract(5, 2) == (5 - 2)


def test_multiply() -> None:
    assert calculator.multiply(3, 2) == (3 * 2)
