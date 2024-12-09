from config import load_config

# Load configuration
config = load_config()
enable_precision = config.get("enable_precision", False)
precision_value = config.get("precision_value", None) if enable_precision else None

def add(a, b):
    """
    Adds two numbers and applies rounding if precision is enabled.
    """
    result = a + b
    if precision_value is not None:
        result = round(result, precision_value)
    return result

def subtract(a, b):
    """
    Subtracts the second number from the first and applies rounding if precision is enabled.
    """
    result = a - b
    if precision_value is not None:
        result = round(result, precision_value)
    return result

def multiply(a, b):
    """
    Multiplies two numbers and applies rounding if precision is enabled.
    """
    result = a * b
    if precision_value is not None:
        result = round(result, precision_value)
    return result

def divide(a, b):
    """
    Divides the first number by the second and applies rounding if precision is enabled.
    Handles division by zero gracefully by raising a ZeroDivisionError.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    result = a / b
    if precision_value is not None:
        result = round(result, precision_value)
    return result
