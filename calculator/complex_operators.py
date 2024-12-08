import math
from config import load_config

# Load configuration
config = load_config()
enable_precision = config.get("enable_precision", False)
precision_value = config.get("precision_value", None) if enable_precision else None

def exponent(base, power):
    """
    Raises the base to the power. Handles undefined cases for real numbers.
    """
    # Rule: 0^0 is undefined
    if base == 0 and power == 0:
        raise ValueError("0^0 is undefined.")
    # Rule: Negative base with non-integer negative power is undefined
    if base < 0 and not power.is_integer():
        raise ValueError("Raising a negative base to a non-integer power is undefined in real numbers.")
    
    result = math.pow(base, power)
    if precision_value is not None:
        result = round(result, precision_value)
    return result

def logarithm(value, base=math.e):
    """
    Calculates the logarithm of a value with the specified base. Enforces the rules of logarithms
    in real numbers.
    """
    # Rule: Value must be positive
    if value <= 0:
        raise ValueError("Logarithm is undefined for non-positive values.")
    # Rule: Base must be positive and not equal to 1
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    
    result = math.log(value, base)
    if precision_value is not None:
        result = round(result, precision_value)
    return result