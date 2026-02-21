"""
calculator.py

A clean, production-style calculator module.
Provides basic arithmetic operations via a CLI interface.
"""

from typing import Callable


class Calculator:
    """Performs basic arithmetic operations."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Return the sum of two numbers."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Return the difference of two numbers."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Return the product of two numbers."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """
        Return the division of two numbers.

        Raises:
            ValueError: If division by zero is attempted.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b


def get_number(prompt: str) -> float:
    """
    Prompt the user for a floating-point number.

    Args:
        prompt: The message shown to the user.

    Returns:
        A valid float entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operation() -> Callable[[float, float], float]:
    """
    Prompt the user to choose an operation.

    Returns:
        A callable calculator method corresponding to the selected operation.
    """
    operations = {
        "1": Calculator.add,
        "2": Calculator.subtract,
        "3": Calculator.multiply,
        "4": Calculator.divide,
    }

    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1-4): ")
        if choice in operations:
            return operations[choice]
        print("Invalid choice. Please select 1-4.")


def main() -> None:
    """Run the calculator CLI application."""
    print("=== Professional Calculator ===")

    number_one = get_number("Enter first number: ")
    number_two = get_number("Enter second number: ")
    operation = get_operation()

    try:
        result = operation(number_one, number_two)
        print(f"\nResult: {result}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()