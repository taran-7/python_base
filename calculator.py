"""
Calculator module with basic mathematical operations.
"""
import math


def calculator(a: float, b: float = 0, operation: str = "+") -> float | str:
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return "Error: division by zero"
            return a / b
        case "%":
            return a * b / 100
        case "sqrt":
            if a < 0:
                return "Error: cannot calculate square root of a negative number"
            return math.sqrt(a)
        case _:
            return f"Error: unknown operation '{operation}'"
