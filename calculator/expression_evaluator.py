from db_log import log_operation
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
    Logs the result or any error that occurs during evaluation.
    """
    try:
        # Map basic operators to functions
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
                return str(apply_precision(trig_operations[func_name](argument)))
            raise ValueError(f"Unsupported function: {func_name}")

        # Replace trigonometric functions with their evaluated results
        expression = re.sub(r'(sin|cos|tan|cot|arcsin|arccos|arctan|arccot)\((-?\d+(\.\d+)?)\)',
                            evaluate_trig, expression)

         # Replace the π symbol with its value
        expression = expression.replace("π", str(pi))

        # Securely evaluate the expression using eval
        allowed_names = {**basic_operations, **trig_operations, "pi": pi}
        code = compile(expression, "<string>", "eval")
        for name in code.co_names:
            if name not in allowed_names:
                raise ValueError(f"Use of '{name}' is not allowed.")

        result = eval(code, {"__builtins__": None}, allowed_names)
        result = apply_precision(result)

        # Log the successful operation
        log_operation("Expression Evaluation", expression, result)

        return result

    except ZeroDivisionError:
        log_operation("Error", expression, "Division by zero")
        raise ValueError("Division by zero is not allowed.")
    except ValueError as ve:
        log_operation("Error", expression, f"Invalid value: {ve}")
        raise ValueError(f"Invalid value: {ve}")
    except Exception as e:
        log_operation("Error", expression, f"Unexpected error: {e}")
        raise ValueError(f"Error evaluating expression: {e}")
