import sqlite3
from datetime import datetime

# Path to the database file
DB_FILE = "calculator_log.db"

def connect_db():
    """
    Connect to the SQLite database. Creates the database and table if they don't exist.
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    # Create the table if it doesn't already exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS operation_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operator TEXT NOT NULL,
            operands TEXT NOT NULL,
            result TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    return connection

def log_operation(operator, operands, result):
    """
    Logs an operation to the database.
    :param operator: The operator used (e.g., addition, sine, logarithm)
    :param operands: The operands used in the operation (e.g., "5, 3")
    :param result: The result of the operation
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO operation_logs (operator, operands, result)
            VALUES (?, ?, ?)
        """, (operator, operands, str(result)))
        connection.commit()
        connection.close()
    except Exception as e:
        print(f"Error logging operation: {e}")
        return "Error"

def fetch_logs():
    """
    Fetches all operation logs from the database.
    :return: A list of log entries
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM operation_logs ORDER BY timestamp DESC")
        logs = cursor.fetchall()
        connection.close()
        return logs
    except Exception as e:
        print(f"Error fetching logs: {e}")
        return []

def clear_logs():
    """
    Deletes all entries from the operation_logs table in the database.
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM operation_logs")  # Deletes all rows in the table
        connection.commit()
        connection.close()
        print("All logs have been successfully cleared.")
    except Exception as e:
        print(f"Failed to clear logs: {e}")
