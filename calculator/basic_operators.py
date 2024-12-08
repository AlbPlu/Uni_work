from config import load_config
from error_handler import handle_error
from db_log import log_operation  # Import the logging function for database

# Load configuration
config = load_config()
enable_precision = config.get("enable_precision", False)
precision_value = config.get("precision_value", None) if enable_precision else None

def add(a, b):
    """
    Adds two numbers, applies rounding if precision is enabled, and logs the operation.
    """
    try:
        result = a + b
        if precision_value is not None:
            result = round(result, precision_value)
        # Log the operation to the database
        log_operation("Addition", f"{a}, {b}", result)
        return result
    except Exception as e:
        handle_error(e, display_to_user=True)

def subtract(a, b):
    """
    Subtracts the second number from the first, applies rounding if precision is enabled, and logs the operation.
    """
    try:
        result = a - b
        if precision_value is not None:
            result = round(result, precision_value)
        # Log the operation to the database
        log_operation("Subtraction", f"{a}, {b}", result)
        return result
    except Exception as e:
        handle_error(e, display_to_user=True)

def multiply(a, b):
    """
    Multiplies two numbers, applies rounding if precision is enabled, and logs the operation.
    """
    try:
        result = a * b
        if precision_value is not None:
            result = round(result, precision_value)
        # Log the operation to the database
        log_operation("Multiplication", f"{a}, {b}", result)
        return result
    except Exception as e:
        handle_error(e, display_to_user=True)

def divide(a, b):
    """
    Divides the first number by the second, applies rounding if precision is enabled, handles division by zero gracefully, and logs the operation.
    """
    try:
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result = a / b
        if precision_value is not None:
            result = round(result, precision_value)
        # Log the operation to the database
        log_operation("Division", f"{a}, {b}", result)
        return result
    except ZeroDivisionError as e:
        handle_error(e, display_to_user=True)
        # Log the error to the database with "Error" as the result
        log_operation("Division", f"{a}, {b}", "Error: Division by zero")
    except Exception as e:
        handle_error(e, display_to_user=True)
        # Log the error to the database with "Error" as the result
        log_operation("Division", f"{a}, {b}", "Error: An unexpected error occurred")