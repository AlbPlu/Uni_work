import math
from config import load_config
from error_handler import handle_error

# Load configuration
config = load_config()
enable_precision = config.get("enable_precision", False)
precision_value = config.get("precision_value", None) if enable_precision else None
angle_unit = config.get("angle_unit", "radians")  # Default to radians

def to_radians(angle):
    """
    Converts an angle to radians if the configuration is set to degrees.
    """
    if angle_unit == "degrees":
        return math.radians(angle)
    return angle

def apply_precision(value):
    """
    Applies precision rounding if enabled.
    """
    if precision_value is not None:
        return round(value, precision_value)
    return value

# Core trigonometric functions
def sin(angle):
    """
    Calculates the sine of an angle (in radians or degrees based on config).
    """
    try:
        angle = to_radians(angle)
        result = math.sin(angle)
        return apply_precision(result)
    except Exception as e:
        handle_error(e, display_to_user=True)
        return "Error: An unexpected error occurred"

def cos(angle):
    """
    Calculates the cosine of an angle (in radians or degrees based on config).
    """
    try:
        angle = to_radians(angle)
        result = math.cos(angle)
        return apply_precision(result)
    except Exception as e:
        handle_error(e, display_to_user=True)
        return "Error: An unexpected error occurred"

def tan(angle):
    """
    Calculates the tangent of an angle (in radians or degrees based on config). Checks for undefined values.
    """
    try:
        angle = to_radians(angle)
        if math.isclose(math.cos(angle), 0, abs_tol=1e-10):
            raise ValueError(" Tangent is undefined at this angle.")
        result = math.tan(angle)
        return apply_precision(result)
    except Exception as e:
        handle_error(e, display_to_user=True)
        return "Error: An unexpected error occurred"

def cot(angle):
    """
    Calculates the cotangent of an angle (in radians or degrees based on config). Checks for undefined values.
    """
    try:
        angle = to_radians(angle)
        if math.isclose(math.sin(angle), 0, abs_tol=1e-10):
            raise ValueError(" Cotangent is undefined at this angle.")
        result = 1 / math.tan(angle)
        return apply_precision(result)
    except Exception as e:
        handle_error(e, display_to_user=True)
        return "Error: An unexpected error occurred"

# Inverse trigonometric functions
def arcsin(value):
    """
    Calculates the arcsine of a value. Ensures the input is within [-1, 1].
    """
    try:
        if not -1 <= value <= 1:
            raise ValueError(" Arcsin is undefined for values outside [-1, 1].")
        result = math.asin(value)
        return apply_precision(result)
    except Exception as e:
        handle_error(e, display_to_user=True)
        return "Error: An unexpected error occurred"

def arccos(value):
    """
    Calculates the arccosine of a value. Ensures the input is within [-1, 1].
    """
    try:
        if not -1 <= value <= 1:
            raise ValueError(" Arccos is undefined for values outside [-1, 1].")
        result = math.acos(value)
        return apply_precision(result)
    except Exception as e:
        handle_error(e, display_to_user=True)
        return "Error: An unexpected error occurred"

def arctan(value):
    """
    Calculates the arctangent of a value.
    """
    try:
        result = math.atan(value)
        return apply_precision(result)
    except Exception as e:
        handle_error(e, display_to_user=True)
        return "Error: An unexpected error occurred"

def arccot(value):
    """
    Calculates the arccotangent of a value.
    """
    try:
        if math.isclose(value, 0, abs_tol=1e-10):
            raise ValueError(" Arccot is undefined for value 0.")
        result = math.atan(1 / value)
        return apply_precision(result)
    except Exception as e:
        handle_error(e, display_to_user=True)
        return "Error: An unexpected error occurred"