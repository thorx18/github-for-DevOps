"""
calculator.py

A simple calculator module that provides basic arithmetic operations.
"""

from typing import Union


class Calculator:
    """A class that performs basic arithmetic operations."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Return the sum of two numbers."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Return the difference between two numbers."""
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
            ValueError: If attempting to divide by zero.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b


def main() -> None:
    """Run the calculator application."""
    calculator = Calculator()

    try:
        num1: float = float(input("Enter first number: "))
        num2: float = float(input("Enter second number: "))

        print("\nResults:")
        print("Addition:", calculator.add(num1, num2))
        print("Subtraction:", calculator.subtract(num1, num2))
        print("Multiplication:", calculator.multiply(num1, num2))
        print("Division:", calculator.divide(num1, num2))

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()