import tkinter as tk
from tkinter import messagebox, font
from expression_evaluator import evaluate_expression
from db_log import reset_logs, fetch_logs

# Initialize the main window first
root = tk.Tk()
root.title("Resizable Calculator")
root.geometry("500x600")  # Initial size

# Configure grid rows and columns for resizing
for i in range(9):  # 9 rows (including Clear and Show Logs)
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # 4 columns
    root.grid_columnconfigure(j, weight=1)

# Initialize display variable
display = tk.StringVar()

def append_to_expression(value):
    """
    Appends a value to the current expression in the display.
    Ensures that multiple operators cannot be added consecutively.
    """
    current_text = display.get()
    operators = set("+-*/^")

    # If the last character is an operator and the new value is also an operator
    if current_text and current_text[-1] in operators and value in operators:
        # Replace the last operator with the new one
        display.set(current_text[:-1] + value)
    else:
        # Otherwise, append the value as normal
        display.set(current_text + str(value))

def clear_expression():
    """
    Clears the current expression.
    """
    display.set("")

def calculate_expression():
    """
    Evaluates the current expression using the evaluator and displays the result.
    Handles errors gracefully.
    """
    try:
        expression = display.get()
        if not expression.strip():  # Handle empty input
            raise ValueError("The expression is empty.")

        print(f"Evaluating: {expression}")  # Debugging
        result = evaluate_expression(expression)  # Calls the centralized evaluator
        display.set(result)  # Display the result in the calculator

    except ValueError as ve:
        # Display user-friendly error messages
        messagebox.showerror("Error", str(ve))
        display.set("")  # Clear the display if there is an error

    except Exception as e:
        # Handle unexpected errors gracefully
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        display.set("")


import tkinter as tk
from tkinter import ttk
from db_log import fetch_logs, reset_logs

def show_logs():
    """
    Opens a new window to display logs in a table format and allows clearing logs.
    Automatically refreshes every 2 seconds.
    """
    def update_logs():
        """
        Updates the table with the latest logs from the database.
        """
        for row in tree.get_children():  # Clear the existing rows
            tree.delete(row)

        logs = fetch_logs()  # Fetch logs from the database
        if logs:
            for log in logs:
                tree.insert("", "end", values=log)  # Insert each log as a row
        else:
            tree.insert("", "end", values=("No logs available", "", "", "", ""))

        logs_window.after(2000, update_logs)  # Schedule the next update

    def clear_logs_action():
        """
        Clears all logs and refreshes the table.
        """
        reset_logs()
        for row in tree.get_children():  # Clear the table rows
            tree.delete(row)
        tree.insert("", "end", values=("No logs available", "", "", "", ""))

    # Create the logs window
    logs_window = tk.Toplevel()
    logs_window.title("Logs")
    logs_window.geometry("800x400")  # Set an appropriate initial size

    # Create the table using Treeview
    columns = ("ID", "Operator", "Expression", "Result", "Timestamp")
    tree = ttk.Treeview(logs_window, columns=columns, show="headings")
    tree.pack(fill="both", expand=True)

    # Configure column headings
    tree.heading("ID", text="ID")
    tree.heading("Operator", text="Operator")
    tree.heading("Expression", text="Expression")
    tree.heading("Result", text="Result")
    tree.heading("Timestamp", text="Timestamp")

    # Set column widths
    tree.column("ID", width=50, anchor="center")
    tree.column("Operator", width=150, anchor="center")
    tree.column("Expression", width=300, anchor="w")
    tree.column("Result", width=150, anchor="center")
    tree.column("Timestamp", width=200, anchor="center")

    # Add a "Clear Logs" button
    clear_logs_btn = tk.Button(logs_window, text="Clear Logs", font=("Arial", 14), command=clear_logs_action)
    clear_logs_btn.pack(fill="x", padx=10, pady=10)

    # Initial log update and start auto-refresh
    update_logs()


def adjust_font(event):
    """
    Dynamically adjusts the button text size based on window size.
    """
    new_size = max(10, int(event.width / 30))
    button_font.config(size=new_size)
    entry_font.config(size=new_size + 4)

# Fonts for dynamic resizing
button_font = font.Font(size=14)
entry_font = font.Font(size=20)

# Display for the calculator
entry = tk.Entry(root, textvariable=display, font=entry_font, justify="right", bd=10, insertwidth=2)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),  # Change the command here
]

for text, row, col in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=button_font, command=calculate_expression)  # Connect "=" button to calculate_expression
    else:
        btn = tk.Button(root, text=text, font=button_font,
                        command=lambda val=text: append_to_expression(val))
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Additional operator buttons
extra_buttons = [
    ("π", 5, 0), ("^", 5, 1), ("(", 5, 2), (")", 5, 3)
]

for text, row, col in extra_buttons:
    btn = tk.Button(root, text=text, font=button_font,
                    command=lambda val=text: append_to_expression(val))
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Trigonometric function buttons
trig_buttons = [
    ("sin", 6, 0), ("cos", 6, 1), ("tan", 6, 2), ("cot", 6, 3),
    ("arcsin", 7, 0), ("arccos", 7, 1), ("arctan", 7, 2), ("arccot", 7, 3)
]

for text, row, col in trig_buttons:
    btn = tk.Button(root, text=text, font=button_font,
                    command=lambda val=text: append_to_expression(val + "("))
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Enlarged Clear and Show Logs buttons
btn_clear = tk.Button(root, text="Clear", font=button_font, command=clear_expression)
btn_clear.grid(row=8, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

btn_show_logs = tk.Button(root, text="Show Logs", font=button_font, command=show_logs)
btn_show_logs.grid(row=8, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)

# Bind the resize event to adjust font size
root.bind("<Configure>", adjust_font)

# Run the main loop
root.mainloop()