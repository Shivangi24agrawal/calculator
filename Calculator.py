import tkinter as t
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.expression = ""
        self.root.bind('<Key>', self.key_press)

        self.entry = t.Entry(root, width=35, borderwidth=5, font=('Montserrat', 18))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '×',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            t.Button(root, text=button, width=5, font=('Montserrat', 18), command=lambda button=button: self.append_to_expression(button)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

       
        t.Button(root, text="Clear", width=20, font=('Segoe UI', 18), command=self.clear_expression).grid(row=row_val, column=0, columnspan=4, padx=10, pady=10)

    def append_to_expression(self, button):
        if button == '=':
            try:
                result = str(eval(self.expression))
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.expression = ""
        elif button == '×':
            self.expression += '*'
        else:
            self.expression += button
        self.entry.delete(0, t.END)
        self.entry.insert(t.END, self.expression)

    def clear_expression(self):
        self.expression = ""
        self.entry.delete(0, t.END)

    def key_press(self, event):
        if event.char.isdigit() or event.char in '+-*/.() ':
            self.append_to_expression(event.char)
        elif event.char == '\r':
            self.append_to_expression('=')
        elif event.char == '\b':
            self.expression = self.expression[:-1]
            self.entry.delete(0, t.END)
            self.entry.insert(t.END, self.expression)

root = t.Tk()
calculator = Calculator(root)
root.mainloop()