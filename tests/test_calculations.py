import pytest

from app.calculation import Calculation, CalculationFactory
from app.operation import Addition, Subtraction, Multiplication, Division


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        (Addition, 10, 5, 15),
        (Subtraction, 10, 5, 5),
        (Multiplication, 10, 5, 50),
        (Division, 10, 5, 2),
    ],
)
def test_calculation_perform(operation, a, b, expected):
    """Test that Calculation performs the selected operation."""
    calculation = Calculation(a, b, operation)
    assert calculation.perform() == expected


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        ("+", 10, 5, 15),
        ("-", 10, 5, 5),
        ("*", 10, 5, 50),
        ("/", 10, 5, 2),
    ],
)
def test_calculation_factory(operation, a, b, expected):
    """Test that CalculationFactory creates the correct calculation."""
    calculation = CalculationFactory.create(a, b, operation)
    assert calculation.perform() == expected