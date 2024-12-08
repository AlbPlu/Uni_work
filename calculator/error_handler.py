import logging
from tkinter import messagebox

def log_error(error_message):
    """
    Logs an error message to the logger.
    """
    try:
        logging.error(error_message)
    except Exception as e:
        # Fallback in case logging fails
        return (f"Logging failed: {e}")

def show_error_popup(error_message):
    """
    Displays an error message to the user via a popup.
    """
    try:
        messagebox.showerror("Error", error_message)
    except Exception as e:
        # Log the failure to show a popup
        logging.error(f"Failed to show error popup: {e}")

def handle_error(error, display_to_user=False):
    """
    Handles an error by logging it and optionally showing it to the user.
    :param error: The error message or exception object.
    :param display_to_user: Boolean to determine if an error popup should be shown.
    """
    error_message = str(error) if error else "An unknown error occurred."
    log_error(error_message)
    if display_to_user:
        return show_error_popup(error_message)