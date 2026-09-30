import pytest

from app.operation import Addition, Subtraction, Multiplication, Division

@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        (Addition, 2, 3, 5),
        (Addition, -2, 3, 1),
        (Addition, 0, 0, 0),
        (Subtraction, 5, 3, 2),
        (Subtraction, -2, 3, -5),
        (Subtraction, 0, 0, 0),
        (Multiplication, 4, 3, 12),
        (Multiplication, -4, 3, -12),
        (Multiplication, 0, 5, 0),
        (Division, 10, 2, 5),
        (Division, -10, 2, -5),
        (Division, 5, 2, 2.5),
    ],
)
def test_operations(operation, a, b, expected):
    """Test arithmetic operations with multiple input scenarios."""
    assert operation.execute(a, b) == expected

def test_division_by_zero():
    """Test that division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        Division.execute(10, 0)