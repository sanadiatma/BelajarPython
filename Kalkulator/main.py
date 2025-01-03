import tkinter as tk
from tkinter import messagebox

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            expression_var.set(result)
            expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
            expression_var.set("")
    elif text == "C":
        expression = ""
        expression_var.set("")
    else:
        expression += text
        expression_var.set(expression)

# Main application
root = tk.Tk()
root.title("Simple Calculator")

expression = ""
expression_var = tk.StringVar()

# Entry field
entry = tk.Entry(root, textvar=expression_var, font=("Arial", 20), justify="right", bd=10, relief=tk.RIDGE)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        btn = tk.Button(root, text=button, font=("Arial", 18), width=5, height=2, relief=tk.RAISED)
        btn.grid(row=i + 1, column=j, padx=5, pady=5)
        btn.bind("<Button-1>", click)

# Run application
root.mainloop()

