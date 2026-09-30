from .calculation import Calculation
from app.operation import Addition, Subtraction, Multiplication, Division


class CalculationFactory:
    """Creates Calculation objects based on the selected operation."""

    @staticmethod
    def create(a, b, operation):
        """Create and return a Calculation object."""
        operations = {
            "+": Addition,
            "-": Subtraction,
            "*": Multiplication,
            "/": Division,
        }

        return Calculation(a, b, operations[operation])