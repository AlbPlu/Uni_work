import math
from config import load_config
from error_handler import handle_error
from db_log import log_operation  # Import the logging function for database

# Load configuration
config = load_config()
enable_precision = config.get("enable_precision", False)
precision_value = config.get("precision_value", None) if enable_precision else None

def exponent(base, power):
    """
    Raises the base to the power. Handles undefined cases for real numbers and logs the operation.
    """
    try:
        # Rule: 0^0 is undefined
        if base == 0 and power == 0:
            raise ValueError("0^0 is undefined.")
        # Rule: Negative base with non-integer negative power is undefined
        if base < 0 and not power.is_integer():
            raise ValueError("Raising a negative base to a non-integer power is undefined in real numbers.")
        
        result = math.pow(base, power)
        if precision_value is not None:
            result = round(result, precision_value)
        
        # Log the operation
        log_operation("Exponentiation", f"Base: {base}, Power: {power}", result)
        return result
    except Exception as e:
        handle_error(e, display_to_user=True)
        log_operation("Exponentiation", f"Base: {base}, Power: {power}", "Error: An unexpected error occurred")
        return "Error"

def logarithm(value, base=math.e):
    """
    Calculates the logarithm of a value with the specified base. Enforces the rules of logarithms
    in real numbers and logs the operation.
    """
    try:
        # Rule: Value must be positive
        if value <= 0:
            raise ValueError("Logarithm is undefined for non-positive values.")
        # Rule: Base must be positive and not equal to 1
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1.")
        
        result = math.log(value, base)
        if precision_value is not None:
            result = round(result, precision_value)
        
        # Log the operation
        log_operation("Logarithm", f"Value: {value}, Base: {base}", result)
        return result
    except Exception as e:
        handle_error(e, display_to_user=True)
        log_operation("Logarithm", f"Value: {value}, Base: {base}", "Error: An unexpected error occurred")
        return "Error"

def nth_root(value, n):
    """
    Calculates the n-th root of a value. Enforces real number rules and logs the operation.
    """
    try:
        # Rule: n cannot be zero
        if n == 0:
            raise ValueError("The index of the root (n) cannot be zero.")
        # Rule: n must be an integer
        if not isinstance(n, int):
            raise ValueError("The index of the root (n) must be an integer.")
        # Rule: Even roots of negative numbers are undefined
        if n % 2 == 0 and value < 0:
            raise ValueError("Even roots of negative numbers are undefined in real numbers.")
        
        # Handle odd roots of negative numbers manually
        if n % 2 != 0 and value < 0:
            result = -((-value) ** (1 / n))  # Take the n-th root of the positive value, then negate
        else:
            result = value ** (1 / n)  # Use the exponentiation operator
        
        if precision_value is not None:
            result = round(result, precision_value)
        
        # Log the operation
        log_operation("Nth Root", f"Value: {value}, Index: {n}", result)
        return result
    
    except Exception as e:
        handle_error(e, display_to_user=True)
        log_operation("Nth Root", f"Value: {value}, Index: {n}", "Error: An unexpected error occurred")
        return "Error"