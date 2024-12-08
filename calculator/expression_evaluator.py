import re
import basic_operators
import complex_operators
import trigonometry
from math import pi
from config import load_config

# Load configuration
config = load_config()
enable_precision = config.get("enable_precision", False)
precision_value = config.get("precision_value", None) if enable_precision else None

def apply_precision(value):
    """
    Applies precision rounding if enabled.
    """
    if precision_value is not None:
        return round(value, precision_value)
    return value

def evaluate_expression(expression):
    """
    Evaluates a mathematical expression, including basic and trigonometric functions.
    :param expression: The input string (e.g., "sin(90)+5")
    :return: The evaluated result.
    """
    try:
        # Map basic operators to their module functions
        basic_operations = {
            "+": basic_operators.add,
            "-": basic_operators.subtract,
            "*": basic_operators.multiply,
            "/": basic_operators.divide,
            "^": complex_operators.exponent
        }

        # Map trigonometric functions to their module implementations
        trig_operations = {
            "sin": trigonometry.sin,
            "cos": trigonometry.cos,
            "tan": trigonometry.tan,
            "cot": trigonometry.cot,
            "arcsin": trigonometry.arcsin,
            "arccos": trigonometry.arccos,
            "arctan": trigonometry.arctan,
            "arccot": trigonometry.arccot,
            "pi": lambda: pi  # Handle 'pi' as a constant
        }

        # Evaluate trigonometric functions first using regex
        def evaluate_trig(match):
            func_name = match.group(1)  # Trigonometric function name
            argument = float(match.group(2))  # Extract the angle or value
            if func_name in trig_operations:
                return str(apply_precision(trig_operations[func_name](argument)))  # Evaluate with precision
            raise ValueError(f"Unsupported function: {func_name}")

        # Replace trigonometric functions with their evaluated results
        expression = re.sub(r'(sin|cos|tan|cot|arcsin|arccos|arctan|arccot)\((-?\d+(\.\d+)?)\)',
                            evaluate_trig, expression)

        # Replace 'pi' with its value
        expression = expression.replace("pi", str(pi))

        # Match and evaluate basic operations (two operands and one operator)
        match = re.match(r'^\s*(-?\d+(\.\d+)?)\s*([-+*/^])\s*(-?\d+(\.\d+)?)\s*$', expression)
        if match:
            operand1, operator, operand2 = float(match.group(1)), match.group(3), float(match.group(4))
            if operator in basic_operations:
                return apply_precision(basic_operations[operator](operand1, operand2))

        # If no valid operation is detected
        raise ValueError("Invalid input or unsupported operation.")

    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")
    return "error"