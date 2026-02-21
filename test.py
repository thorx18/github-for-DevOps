"""
calculator.py

A production-grade CLI calculator application.
Provides basic arithmetic operations using command-line arguments.
"""

import argparse
import logging
import sys
from typing import Callable, Dict


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class Calculator:
    """Performs arithmetic operations."""

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


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        Parsed arguments namespace.
    """
    parser = argparse.ArgumentParser(
        description="A professional CLI calculator."
    )

    parser.add_argument("operation", choices=["add", "sub", "mul", "div"],
                        help="Operation to perform")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")

    return parser.parse_args()


def get_operation_map() -> Dict[str, Callable[[float, float], float]]:
    """
    Map operation names to calculator methods.

    Returns:
        Dictionary of operation mappings.
    """
    return {
        "add": Calculator.add,
        "sub": Calculator.subtract,
        "mul": Calculator.multiply,
        "div": Calculator.divide,
    }


def main() -> None:
    """Application entry point."""
    args = parse_arguments()
    operations = get_operation_map()

    try:
        operation_func = operations[args.operation]
        result = operation_func(args.num1, args.num2)
        logging.info("Result: %s", result)
    except ValueError as error:
        logging.error("Error: %s", error)
        sys.exit(1)


if __name__ == "__main__":
    main()