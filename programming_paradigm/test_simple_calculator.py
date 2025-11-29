import sys
from simple_calculator import *


def main ():
    if len(sys.argv) != 3:
        print("Usage: python test_simple_calculator.py <num1> <num2>")
        sys.exit(1)

    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

    calculator = SimpleCalculator()

    print(f"Addition: {calculator.add(num1, num2)}")
    print(f"Subtraction: {calculator.subtract(num1, num2)}")
    print(f"Multiplication: {calculator.multiply(num1, num2)}")
    division_result = calculator.divide(num1, num2)
    if division_result is None:
        print("Division: Error - Cannot divide by zero.")
    else:
        print(f"Division: {division_result}")