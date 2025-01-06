import tkinter as tk
<<<<<<< HEAD
from tkinter import messagebox, font
from expression_evaluator import evaluate_expression
from db_log import reset_logs, fetch_logs

# Initialize the main window first
=======
from tkinter import messagebox, font, ttk
from expression_evaluator import evaluate_expression
from db_log import fetch_logs, reset_logs, delete_log, reorganize_ids

# Initialize the main window
>>>>>>> develop
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

<<<<<<< HEAD
    # If the last character is an operator and the new value is also an operator
=======
>>>>>>> develop
    if current_text and current_text[-1] in operators and value in operators:
        # Replace the last operator with the new one
        display.set(current_text[:-1] + value)
    else:
<<<<<<< HEAD
       # Automatically insert '*' if necessary
=======
        # Automatically insert '*' if necessary
>>>>>>> develop
        if (
            current_text
            and (current_text[-1].isdigit() or current_text[-1] == "π" or current_text[-1] == ")")
            and (value.startswith("(") or value.startswith("sin") or value.startswith("cos")
                 or value.startswith("tan") or value.startswith("cot") or value.startswith("arcsin")
                 or value.startswith("arccos") or value.startswith("arctan") or value.startswith("arccot"))
        ):
            display.set(current_text + "*" + str(value))
        else:
<<<<<<< HEAD
            # Otherwise, append the value as normal
=======
>>>>>>> develop
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
<<<<<<< HEAD
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
=======
        if not expression.strip():
            raise ValueError("The expression is empty.")
        result = evaluate_expression(expression)
        display.set(result)
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
        display.set("")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        display.set("")

def show_logs():
    """
    Opens a new window to display logs in a table format and allows clearing all or selected logs.
>>>>>>> develop
    Automatically refreshes every 2 seconds.
    """
    def update_logs():
        """
        Updates the table with the latest logs from the database.
<<<<<<< HEAD
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
=======
        Preserves the current selection, if valid.
        """
        selected = tree.selection()
        selected_id = None
        if selected:
            selected_log = tree.item(selected[0])["values"]
            if selected_log:
                selected_id = selected_log[0]

        # Clear the existing rows
        for row in tree.get_children():
            tree.delete(row)

        # Fetch and populate logs
        logs = fetch_logs()
        if logs:
            for log in logs:
                tree.insert("", "end", values=log)
        else:
            tree.insert("", "end", values=("No logs available", "", "", "", ""))

        # Restore the selection if the ID still exists
        if selected_id is not None:
            for item in tree.get_children():
                if tree.item(item)["values"][0] == selected_id:
                    tree.selection_set(item)
                    break

        # Schedule the next update
        logs_window.after(2000, update_logs)
>>>>>>> develop

    def clear_logs_action():
        """
        Clears all logs and refreshes the table.
        """
<<<<<<< HEAD
        reset_logs()
        for row in tree.get_children():  # Clear the table rows
            tree.delete(row)
        tree.insert("", "end", values=("No logs available", "", "", "", ""))
=======
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all logs?"):
            reset_logs()
            reorganize_ids()  # Reorganize IDs after clearing logs
            update_logs()

    def clear_selected_log():
        """
        Deletes the selected log and refreshes the table.
        """
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "No log selected.")
            return

        selected_log = tree.item(selected[0])["values"]
        if not selected_log or selected_log[0] == "No logs available":
            messagebox.showwarning("Warning", "Invalid selection.")
            return

        log_id = selected_log[0]
        try:
            delete_log(log_id)
            reorganize_ids()  # Reorganize IDs after deleting a log
            update_logs()
            messagebox.showinfo("Success", f"Log ID {log_id} deleted and IDs updated.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete log ID {log_id}: {e}")
>>>>>>> develop

    # Create the logs window
    logs_window = tk.Toplevel()
    logs_window.title("Logs")
<<<<<<< HEAD
    logs_window.geometry("850x400")  # Set an appropriate initial size
=======
    logs_window.geometry("800x450")  # Set an appropriate initial size
>>>>>>> develop

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

<<<<<<< HEAD
    # Add a "Clear Logs" button
    clear_logs_btn = tk.Button(logs_window, text="Clear Logs", font=("Arial", 14), command=clear_logs_action)
    clear_logs_btn.pack(fill="x", padx=10, pady=10)
=======
    # Add buttons for clearing logs
    btn_clear_selected = tk.Button(logs_window, text="Clear Selected", font=("Arial", 14), command=clear_selected_log)
    btn_clear_selected.pack(side="left", fill="x", expand=True, padx=10, pady=10)

    btn_clear_all = tk.Button(logs_window, text="Clear All", font=("Arial", 14), command=clear_logs_action)
    btn_clear_all.pack(side="right", fill="x", expand=True, padx=10, pady=10)
>>>>>>> develop

    # Initial log update and start auto-refresh
    update_logs()

<<<<<<< HEAD

=======
>>>>>>> develop
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
<<<<<<< HEAD
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),  # Change the command here
=======
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
>>>>>>> develop
]

for text, row, col in buttons:
    if text == "=":
<<<<<<< HEAD
        btn = tk.Button(root, text=text, font=button_font, command=calculate_expression)  # Connect "=" button to calculate_expression
    else:
        btn = tk.Button(root, text=text, font=button_font,
                        command=lambda val=text: append_to_expression(val))
=======
        btn = tk.Button(root, text=text, font=button_font, command=calculate_expression)
    else:
        btn = tk.Button(root, text=text, font=button_font, command=lambda val=text: append_to_expression(val))
>>>>>>> develop
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Additional operator buttons
extra_buttons = [
    ("π", 5, 0), ("^", 5, 1), ("(", 5, 2), (")", 5, 3)
]

for text, row, col in extra_buttons:
<<<<<<< HEAD
    btn = tk.Button(root, text=text, font=button_font,
                    command=lambda val=text: append_to_expression(val))
=======
    btn = tk.Button(root, text=text, font=button_font, command=lambda val=text: append_to_expression(val))
>>>>>>> develop
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Trigonometric function buttons
trig_buttons = [
    ("sin", 6, 0), ("cos", 6, 1), ("tan", 6, 2), ("cot", 6, 3),
    ("arcsin", 7, 0), ("arccos", 7, 1), ("arctan", 7, 2), ("arccot", 7, 3)
]

for text, row, col in trig_buttons:
<<<<<<< HEAD
    btn = tk.Button(root, text=text, font=button_font,
                    command=lambda val=text: append_to_expression(val + "("))
=======
    btn = tk.Button(root, text=text, font=button_font, command=lambda val=text: append_to_expression(val + "("))
>>>>>>> develop
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Enlarged Clear and Show Logs buttons
btn_clear = tk.Button(root, text="Clear", font=button_font, command=clear_expression)
btn_clear.grid(row=8, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

btn_show_logs = tk.Button(root, text="Show Logs", font=button_font, command=show_logs)
btn_show_logs.grid(row=8, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)

# Bind the resize event to adjust font size
root.bind("<Configure>", adjust_font)

# Run the main loop
<<<<<<< HEAD
root.mainloop()
=======
root.mainloop()
>>>>>>> develop
