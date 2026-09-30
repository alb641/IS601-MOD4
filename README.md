# IS601 Module 4 - Python Calculator

For Module 4, I built a command-line calculator using Python. The calculator can do addition, subtraction, multiplication, and division.

The project is separated into different files/classes so that each part has its own job. I also added a calculation history, help and exit commands, input validation, error handling, tests, and GitHub Actions.

## The calculator supports:

* `+` Addition
* `-` Subtraction
* `*` Multiplication
* `/` Division
* `history` to see previous calculations
* `help` to see the available commands
* `exit` to close the calculator

It also handles things like entering something that isn't a number and trying to divide by zero without crashing the program.

## Project Structure

```text
IS601-MOD4/
├── .github/
│   └── workflows/
│       └── python-app.yml
├── app/
│   ├── __init__.py
│   ├── calculator/
│   │   ├── __init__.py
│   │   └── calculator.py
│   ├── calculation/
│   │   ├── __init__.py
│   │   ├── calculation.py
│   │   └── factory.py
│   └── operation/
│       ├── __init__.py
│       ├── addition.py
│       ├── division.py
│       ├── multiplication.py
│       └── subtraction.py
├── tests/
│   ├── test_calculations.py
│   ├── test_calculator.py
│   └── test_operations.py
└── README.md
```

## Setup

First, create a virtual environment:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

Then install pytest and pytest-cov:

```powershell
python -m pip install --upgrade pip
pip install pytest pytest-cov
```

## Running the Calculator

From the main project folder, run:

```powershell
python app/calculator/calculator.py
```

The calculator will ask for a command.

For example:

```text
Welcome to the Calculator!
Type 'help' for available commands.

Enter command: +
Enter first number: 10
Enter second number: 5
Result: 15.0
```

You can then use `history` to see the calculations from the current session.

## Testing

I used pytest to test the different parts of the calculator.

To run all tests:

```powershell
python -m pytest
```

To run the tests with coverage:

```powershell
python -m pytest --cov=app --cov-report=term-missing
```

The final test results were:

```text
36 passed
100% coverage
```

The tests include the individual operations, calculations, calculator commands, history, invalid commands, invalid numbers, and division by zero.

## Error Handling

The calculator checks for invalid input so that the program doesn't crash when the user enters something wrong.

For example, if the user enters letters instead of a number, the calculator displays an error and allows the user to continue.

Division by zero is also checked before trying to perform the calculation.

This project demonstrates both LBYL (Look Before You Leap) and EAFP (Easier to Ask Forgiveness than Permission) approaches to handling errors.

## CalculationFactory

I used a `CalculationFactory` to create the correct calculation based on the operation the user selects.

For example, if the user enters `+`, the factory creates an addition calculation. This keeps the different parts of the calculator separated instead of putting all of the operation logic into one file.

## Problems I Ran Into

I had a few issues while setting up the project.

One issue was that I originally had `calculation.py` in the wrong folder. It was inside the `calculator` folder instead of the `calculation` folder. This caused an import error because Python couldn't find `app.calculation.calculation`.

I also had an issue where pytest couldn't find the `app` module. My regular Python imports were working, but running `pytest` gave a `ModuleNotFoundError`. I fixed this by making sure the `app` package was set up correctly and using:

```powershell
python -m pytest
```

instead of just `pytest`.

I also had an issue when connecting my local repository to GitHub because the GitHub repository already had a commit. I had to pull the existing commit using `--allow-unrelated-histories` before I could push my local project.

After fixing these issues, the tests were able to run correctly.

## GitHub Actions

I added a GitHub Actions workflow that automatically runs the tests when changes are pushed to `main` or when a pull request is created.

The workflow installs the required dependencies, runs pytest with coverage, and checks that the project has at least 100% test coverage.

The final GitHub Actions check passed successfully.
