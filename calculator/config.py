import json
import logging
from error_handler import handle_error

def load_config(config_file="config.json"):
    """
    Loads configuration from a JSON file with error handling.
    :param config_file: Path to the configuration file.
    :return: A dictionary containing the configuration.
    """
    try:
        with open(config_file, "r") as file:
            config = json.load(file)
            return clean_config(config)
    except FileNotFoundError as e:
        handle_error(f"Configuration file '{config_file}' not found: {e}", display_to_user=False)
    except json.JSONDecodeError as e:
        handle_error(f"Malformed configuration file: {e}", display_to_user=False)
    except Exception as e:
        handle_error(f"Unexpected error while loading config: {e}", display_to_user=False)
    
    logging.warning("Using default configuration as fallback.")
    return {
        "enable_precision": False,
        "precision_value": None
    }

def clean_config(config):
    """
    Cleans and validates the configuration by removing unused keys and ensuring defaults.
    """
    if not config.get("enable_precision", False):
        config.pop("precision_value", None)
    
    # Ensure defaults
    config.setdefault("enable_precision", False)
    config.setdefault("precision_value", 2 if config["enable_precision"] else None)

    # Validate keys and types
    required_keys = {
        "enable_precision": bool,
        "precision_value": (int, type(None))
    }

    for key, expected_type in required_keys.items():
        if key not in config:
            raise ValueError(f"Missing required configuration key: '{key}'")
        if not isinstance(config[key], expected_type):
            raise ValueError(
                f"Invalid type for key '{key}': Expected {expected_type}, got {type(config[key])}"
            )
    
    return config