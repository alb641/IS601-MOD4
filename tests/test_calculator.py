import pytest

from app.calculator import Calculator


def test_calculator_addition():
    """Test calculator addition and history."""
    calculator = Calculator()

    result = calculator.calculate(10, 5, "+")

    assert result == 15
    assert calculator.history == ["10 + 5 = 15"]


def test_calculator_subtraction():
    """Test calculator subtraction."""
    calculator = Calculator()

    result = calculator.calculate(10, 5, "-")

    assert result == 5


def test_calculator_multiplication():
    """Test calculator multiplication."""
    calculator = Calculator()

    result = calculator.calculate(10, 5, "*")

    assert result == 50


def test_calculator_division():
    """Test calculator division."""
    calculator = Calculator()

    result = calculator.calculate(10, 5, "/")

    assert result == 2


def test_empty_history(capsys):
    """Test history when no calculations exist."""
    calculator = Calculator()

    calculator.show_history()

    captured = capsys.readouterr()
    assert "No calculations in history." in captured.out


def test_history(capsys):
    """Test displaying calculation history."""
    calculator = Calculator()
    calculator.calculate(10, 5, "+")

    calculator.show_history()

    captured = capsys.readouterr()
    assert "Calculation History:" in captured.out
    assert "10 + 5 = 15" in captured.out


def test_help(capsys):
    """Test help command output."""
    Calculator.show_help()

    captured = capsys.readouterr()

    assert "Available commands:" in captured.out
    assert "history" in captured.out
    assert "help" in captured.out
    assert "exit" in captured.out


def test_run_exit(monkeypatch, capsys):
    """Test exiting the calculator."""
    calculator = Calculator()

    monkeypatch.setattr("builtins.input", lambda _: "exit")

    calculator.run()

    captured = capsys.readouterr()
    assert "Welcome to the Calculator!" in captured.out
    assert "Goodbye!" in captured.out


def test_run_invalid_command_then_exit(monkeypatch, capsys):
    """Test invalid command handling."""
    calculator = Calculator()

    inputs = iter(["invalid", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator.run()

    captured = capsys.readouterr()
    assert "Invalid command." in captured.out


def test_run_help_then_exit(monkeypatch, capsys):
    """Test help command in the REPL."""
    calculator = Calculator()

    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator.run()

    captured = capsys.readouterr()
    assert "Available commands:" in captured.out


def test_run_history_then_exit(monkeypatch, capsys):
    """Test history command in the REPL."""
    calculator = Calculator()

    inputs = iter(["history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator.run()

    captured = capsys.readouterr()
    assert "No calculations in history." in captured.out


def test_run_calculation(monkeypatch, capsys):
    """Test performing a calculation through the REPL."""
    calculator = Calculator()

    inputs = iter(["+", "10", "5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator.run()

    captured = capsys.readouterr()
    assert "Result: 15.0" in captured.out


def test_run_division_by_zero(monkeypatch, capsys):
    """Test division by zero handling in the REPL."""
    calculator = Calculator()

    inputs = iter(["/", "10", "0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator.run()

    captured = capsys.readouterr()
    assert "Cannot divide by zero." in captured.out


def test_run_invalid_number(monkeypatch, capsys):
    """Test invalid number handling in the REPL."""
    calculator = Calculator()

    inputs = iter(["+", "abc", "5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator.run()

    captured = capsys.readouterr()
    assert "Please enter valid numbers." in captured.out

def test_main_block(monkeypatch):
    """Test the calculator main entry point."""
    monkeypatch.setattr("builtins.input", lambda _: "exit")

    with open("app/calculator/calculator.py", encoding="utf-8") as file:
        code = compile(file.read(), "app/calculator/calculator.py", "exec")

    exec(code, {"__name__": "__main__"})