import math
from config import load_config
from error_handler import handle_error
from db_log import log_operation  # Import the logging function for database

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
    Calculates the sine of an angle (in radians or degrees based on config) and logs the operation.
    """
    try:
        angle = to_radians(angle)
        result = math.sin(angle)
        result = apply_precision(result)
        log_operation("Sine", f"Angle: {angle} (radians)", result)
        return result
    except Exception as e:
        handle_error(e, display_to_user=True)
        log_operation("Sine", f"Angle: {angle} (radians)", "Error: An unexpected error occurred")
        return "Error"

def cos(angle):
    """
    Calculates the cosine of an angle (in radians or degrees based on config) and logs the operation.
    """
    try:
        angle = to_radians(angle)
        result = math.cos(angle)
        result = apply_precision(result)
        log_operation("Cosine", f"Angle: {angle} (radians)", result)
        return result
    except Exception as e:
        handle_error(e, display_to_user=True)
        log_operation("Cosine", f"Angle: {angle} (radians)", "Error: An unexpected error occurred")
        return "Error"

def tan(angle):
    """
    Calculates the tangent of an angle (in radians or degrees based on config). Checks for undefined values and logs the operation.
    """
    try:
        angle = to_radians(angle)
        if math.isclose(math.cos(angle), 0, abs_tol=1e-10):
            raise ValueError("Tangent is undefined at this angle.")
        result = math.tan(angle)
        result = apply_precision(result)
        log_operation("Tangent", f"Angle: {angle} (radians)", result)
        return result
    except Exception as e:
        handle_error(e, display_to_user=True)
        log_operation("Tangent", f"Angle: {angle} (radians)", "Error: An unexpected error occurred")
        return "Error"

def cot(angle):
    """
    Calculates the cotangent of an angle (in radians or degrees based on config). Checks for undefined values and logs the operation.
    """
    try:
        angle = to_radians(angle)
        if math.isclose(math.sin(angle), 0, abs_tol=1e-10):
            raise ValueError("Cotangent is undefined at this angle.")
        result = 1 / math.tan(angle)
        result = apply_precision(result)
        log_operation("Cotangent", f"Angle: {angle} (radians)", result)
        return result
    except Exception as e:
        handle_error(e, display_to_user=True)
        log_operation("Cotangent", f"Angle: {angle} (radians)", "Error: An unexpected error occurred")
        return "Error"

# Inverse trigonometric functions
def arcsin(value):
    """
    Calculates the arcsine of a value. Ensures the input is within [-1, 1] and logs the operation.
    """
    try:
        if not -1 <= value <= 1:
            raise ValueError("Arcsin is undefined for values outside [-1, 1].")
        result = math.asin(value)
        result = apply_precision(result)
        log_operation("Arcsine", f"Value: {value}", result)
        return result
    except Exception as e:
        handle_error(e, display_to_user=True)
        log_operation("Arcsine", f"Value: {value}", "Error: An unexpected error occurred")
        return "Error"

def arccos(value):
    """
    Calculates the arccosine of a value. Ensures the input is within [-1, 1] and logs the operation.
    """
    try:
        if not -1 <= value <= 1:
            raise ValueError("Arccos is undefined for values outside [-1, 1].")
        result = math.acos(value)
        result = apply_precision(result)
        log_operation("Arccosine", f"Value: {value}", result)
        return result
    except Exception as e:
        handle_error(e, display_to_user=True)
        log_operation("Arccosine", f"Value: {value}", "Error: An unexpected error occurred")
        return "Error"

def arctan(value):
    """
    Calculates the arctangent of a value and logs the operation.
    """
    try:
        result = math.atan(value)
        result = apply_precision(result)
        log_operation("Arctangent", f"Value: {value}", result)
        return result
    except Exception as e:
        handle_error(e, display_to_user=True)
        log_operation("Arctangent", f"Value: {value}", "Error: An unexpected error occurred")
        return "Error"

def arccot(value):
    """
    Calculates the arccotangent of a value and logs the operation.
    """
    try:
        if math.isclose(value, 0, abs_tol=1e-10):
            raise ValueError("Arccot is undefined for value 0.")
        result = math.atan(1 / value)
        result = apply_precision(result)
        log_operation("Arccotangent", f"Value: {value}", result)
        return result
    except Exception as e:
        handle_error(e, display_to_user=True)
        log_operation("Arccotangent", f"Value: {value}", "Error: An unexpected error occurred")
        return "Error"