import tkinter as tk
import math

def calculate(expression):
    try:
        expression = preprocess_expression(expression)
        result = eval(expression, {"__builtins__": None}, {"math": math})
        return round(result, 10)  # Round to 10 decimal places
    except ZeroDivisionError:
        raise ValueError("Error: Division by zero")
    except Exception as e:
        raise ValueError(f"Error: {str(e)}")

def preprocess_expression(expression):
    # Ensure proper conversion from degrees to radians
    expression = expression.replace('sin(', 'math.sin(math.radians(')
    expression = expression.replace('cos(', 'math.cos(math.radians(')
    expression = expression.replace('tan(', 'math.tan(math.radians(')

    # Wrap the entire expression in parentheses
    expression = f"({expression})"

    # Count parentheses to balance them
    opening_parentheses = expression.count('(')
    closing_parentheses = expression.count(')')
    
    # Add closing parentheses for any unmatched opening parentheses
    expression += ')' * (opening_parentheses - closing_parentheses)
    
    return expression

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Calculator")

    # Entry for input and display
    entry = create_entry(root)

    # Define calculator buttons
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+',
        'C', 'Del',
        'sin(', 'cos(', 'tan(',
        '(', ')',
        'inv'  # Inverse button
    ]

    # Create buttons and arrange them in the grid
    row_val = 1
    col_val = 0

    for button in buttons:
        create_button(root, entry, button, row_val, col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    # Run the main loop
    root.mainloop()

def create_entry(root):
    entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=5, relief="ridge", justify="right")
    entry.grid(row=0, column=0, columnspan=4)
    return entry

def create_button(root, entry, symbol, row_val, col_val):
    tk.Button(root, text=symbol, width=4, height=2, font=('Arial', 18),
              command=lambda: button_command(entry, symbol)).grid(row=row_val, column=col_val)

def button_command(entry, symbol):
    if symbol == '=':
        calculate_and_display(entry)
    elif symbol == 'Del':
        delete_last(entry)
    elif symbol == 'C':
        clear_entry(entry)
    elif symbol == 'inv':
        calculate_inverse_and_display(entry)
    else:
        button_click(entry, str(symbol))

def calculate_and_display(entry):
    try:
        result = calculate(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except ValueError as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(e))

def calculate_inverse_and_display(entry):
    try:
        current_result = float(entry.get())
        result = 1 / current_result
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except ValueError as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(e))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: Division by zero")

def button_click(entry, symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(symbol))

def clear_entry(entry):
    entry.delete(0, tk.END)

def delete_last(entry):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text[:-1])

# Run the main function
if __name__ == "__main__":
    main()
