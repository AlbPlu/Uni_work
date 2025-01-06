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
    # Create the table with the correct schema
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS operation_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operator TEXT NOT NULL,   -- The operation type (e.g., "Expression Evaluation")
            expression TEXT NOT NULL, -- The full mathematical expression
            result TEXT NOT NULL,     -- The result of the evaluation
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    return connection


def log_operation(operator, expression, result):
    """
    Logs an operation to the database.
    :param operator: The operator type (e.g., "Expression Evaluation")
    :param expression: The full mathematical expression
    :param result: The result of the operation
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO operation_logs (operator, expression, result)
            VALUES (?, ?, ?)
        """, (operator, expression, str(result)))
        connection.commit()
        connection.close()
    except Exception as e:
        print(f"Error logging operation: {e}")

<<<<<<< HEAD
=======

>>>>>>> develop
def fetch_logs():
    """
    Fetches all operation logs from the database.
    :return: A list of log entries
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM operation_logs ORDER BY timestamp ASC")
        logs = cursor.fetchall()
        connection.close()
        return logs
    except Exception as e:
        print(f"Error fetching logs: {e}")
        return []

<<<<<<< HEAD
=======

>>>>>>> develop
def reset_logs():
    """
    Deletes all entries from the operation_logs table and resets the id counter.
    """
    try:
        connection = connect_db()  # Establish database connection
        cursor = connection.cursor()
        # Delete all rows in the operation_logs table
        cursor.execute("DELETE FROM operation_logs")
        # Reset the autoincrement counter for the id column
        cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'operation_logs'")
        connection.commit()  # Commit changes
        connection.close()  # Close the connection
        print("All logs have been cleared and the ID counter has been reset.")
    except Exception as e:
        print(f"Failed to reset logs: {e}")
<<<<<<< HEAD
=======


def delete_log(log_id):
    """
    Deletes a specific log entry from the database by its ID.
    :param log_id: The ID of the log to delete.
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM operation_logs WHERE id = ?", (log_id,))
        connection.commit()
        connection.close()
        print(f"Log with ID {log_id} has been deleted.")
    except Exception as e:
        print(f"Error deleting log with ID {log_id}: {e}")


def reorganize_ids():
    """
    Renumbers the IDs in the operation_logs table to ensure they are sequential.
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()

        # Step 1: Create a temporary table with sequential IDs
        cursor.execute("""
            CREATE TEMPORARY TABLE temp_logs AS
            SELECT operator, expression, result, timestamp FROM operation_logs ORDER BY id
        """)

        # Step 2: Delete all rows from the original table
        cursor.execute("DELETE FROM operation_logs")

        # Step 3: Insert rows back with sequential IDs
        cursor.execute("""
            INSERT INTO operation_logs (id, operator, expression, result, timestamp)
            SELECT ROW_NUMBER() OVER (ORDER BY ROWID) AS id, operator, expression, result, timestamp
            FROM temp_logs
        """)

        # Step 4: Drop the temporary table
        cursor.execute("DROP TABLE temp_logs")

        # Step 5: Reset the AUTOINCREMENT counter
        cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'operation_logs'")

        connection.commit()
        connection.close()
        print("IDs reorganized successfully.")
    except Exception as e:
        print(f"Error reorganizing IDs: {e}")
>>>>>>> develop
