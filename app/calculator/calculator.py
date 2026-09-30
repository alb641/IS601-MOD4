from app.calculation import CalculationFactory


class Calculator:
    """Interactive calculator with command history."""

    def __init__(self):
        """Initialize the calculator and empty history."""
        self.history = []

    def calculate(self, a, b, operation):
        """Perform a calculation and save it to history."""
        calculation = CalculationFactory.create(a, b, operation)
        result = calculation.perform()
        self.history.append(f"{a} {operation} {b} = {result}")
        return result

    def show_history(self):
        """Display all calculations from the current session."""
        if not self.history:
            print("No calculations in history.")
            return

        print("\nCalculation History:")
        for item in self.history:
            print(item)

    @staticmethod
    def show_help():
        """Display available calculator commands."""
        print("\nAvailable commands:")
        print("  +  Addition")
        print("  -  Subtraction")
        print("  *  Multiplication")
        print("  /  Division")
        print("  history  Show calculation history")
        print("  help     Show this help message")
        print("  exit     Exit the calculator")

    def run(self):
        """Run the calculator REPL."""
        print("Welcome to the Calculator!")
        print("Type 'help' for available commands.")

        while True:
            command = input("\nEnter command: ").strip().lower()

            if command == "exit":
                print("Goodbye!")
                break

            if command == "help":
                self.show_help()
                continue

            if command == "history":
                self.show_history()
                continue

            if command not in {"+", "-", "*", "/"}:
                print("Invalid command. Type 'help' for available commands.")
                continue

            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if command == "/" and b == 0:
                    print("Error: Cannot divide by zero.")
                    continue

                result = self.calculate(a, b, command)
                print(f"Result: {result}")

            except ValueError:
                print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    Calculator().run()