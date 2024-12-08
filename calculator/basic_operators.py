from config import load_config
from error_handler import handle_error

# Load configuration
config = load_config()
enable_precision = config.get("enable_precision", False)
precision_value = config.get("precision_value", None) if enable_precision else None

def add(a, b):
    """
    Adds two numbers and applies rounding if precision is enabled.
    """
    try:
        result = a + b
        if precision_value is not None:
            return round(result, precision_value)
        return result
    except Exception as e:
        handle_error(e, display_to_user=True)

def subtract(a, b):
    """
    Subtracts the second number from the first and applies rounding if precision is enabled.
    """
    try:
        result = a - b
        if precision_value is not None:
            return round(result, precision_value)
        return result
    except Exception as e:
        handle_error(e, display_to_user=True)

def multiply(a, b):
    """
    Multiplies two numbers and applies rounding if precision is enabled.
    """
    try:
        result = a * b
        if precision_value is not None:
            return round(result, precision_value)
        return result
    except Exception as e:
        handle_error(e, display_to_user=True)

def divide(a, b):
    """
    Divides the first number by the second and applies rounding if precision is enabled.
    Handles division by zero gracefully.
    """
    try:
        if b == 0:
            raise ZeroDivisionError(" Division by zero is not allowed.")
        result = a / b
        if precision_value is not None:
            return round(result, precision_value)
        return result
    except ZeroDivisionError as e:
        handle_error(e, display_to_user=True)
        return "Error: Division by zero"
    except Exception as e:
        handle_error(e, display_to_user=True)
        return "Error: An unexpected error occurred"