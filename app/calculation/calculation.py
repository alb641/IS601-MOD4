class Calculation:
    """Represents a calculation with two numbers and an operation."""

    def __init__(self, a, b, operation):
        """Initialize a calculation."""
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self):
        """Perform the calculation and return the result."""
        return self.operation.execute(self.a, self.b)