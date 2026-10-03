import math
import tkinter as tk
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("430x560")
        self.root.resizable(False, False)
        self.expression = ""
        self.last_result = None
        self.history = []

        # ----- DISPLAY -----
        self.display = tk.Entry(
            root,
            font=("Arial", 28),
            justify="right",
            bd=0,
            bg="#202124",
            fg="white",
            insertbackground="white"
        )
        self.display.pack(
            fill="both",
            padx=15,
            pady=(20,10),
            ipady=20
        )

        # ---- BUTTON FRAME -----
        button_frame = tk.Frame(root, bg="#202124")
        button_frame.pack(fill="both", expand=True, padx=10, pady=10)
        buttons = [
            [
                ("sin", self.sin),
                ("cos", self.cos),
                ("tan", self.tan),
                ("√", self.square_root),
            ],
            [
                ("asin", self.asin),
                ("acos", self.acos),
                ("atan", self.atan),
                ("xʸ", self.power),
            ],
            [
                ("(", lambda: self.add_to_expression("(")),
                (")", lambda: self.add_to_expression(")")),
                ("ANS", self.answer),
                ("HIST", self.show_history),
            ],
            [
                ("C", self.clear),
                ("⌫", self.backspace),
                ("÷", lambda: self.add_to_expression("/")),
                ("×", lambda: self.add_to_expression("*")),
            ],
            [
                ("7", lambda: self.add_to_expression("7")),
                ("8", lambda: self.add_to_expression("8")),
                ("9", lambda: self.add_to_expression("9")),
                ("-", lambda: self.add_to_expression("-")),
            ],
            [
                ("4", lambda: self.add_to_expression("4")),
                ("5", lambda: self.add_to_expression("5")),
                ("6", lambda: self.add_to_expression("6")),
                ("+", lambda: self.add_to_expression("+")),
            ],
            [
                ("1", lambda: self.add_to_expression("1")),
                ("2", lambda: self.add_to_expression("2")),
                ("3", lambda: self.add_to_expression("3")),
                ("=", self.calculate),
            ],
            [
                ("0", lambda: self.add_to_expression("0")),
                (".", lambda: self.add_to_expression("."))
            ]
        ]

        for row, button_row in enumerate(buttons):
            for col, (text, command) in enumerate(button_row):
                if text == "":
                    continue
                button = tk.Button(
                    button_frame,
                    text=text,
                    command=command,
                    font=("Arial", 15, "bold"),
                    bg="#303134",
                    fg="white",
                    activebackground="#5f6368",
                    activeforeground="white",
                    bd=0
                )
                button.grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=4,
                    pady=4
                )
        for i in range(4):
            button_frame.columnconfigure(i, weight=1)
        for i in range(8):
            button_frame.rowconfigure(i, weight=1)

        # KEYBOARD BINDINGS
        self.root.bind("<Return>", lambda event: self.calculate())
        self.root.bind("<BackSpace>", lambda event: self.backspace())
        self.root.bind("<Escape>", lambda event: self.clear())

    # ----- BASIC INPUT -----
    def add_to_expression(self, value):
        self.expression += value
        self.update_display()
    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)
    def clear(self):
        self.expression = ""
        self.update_display()
    def backspace(self):
        self.expression = self.expression[:-1]
        self.update_display()

    # ----- ANSWER -----
    def answer(self):
        if self.last_result is not None:
            self.expression += str(self.last_result)
            self.update_display()

    # ----- CALCULATIONS -----
    def calculate(self):
        if not self.expression:
            return
        try:
            expression = self.expression.replace("^", "**")
            result = eval( 
                expression, {
                    "_builtins_":{},
                    "math":math
            }
            )
            result = round(result, 6)
            record = f"{self.expression} = {result}"
            self.history.append(record)
            if len(self.history) > 10:
                self.history.pop(0)
            self.last_result = result
            self.expression = str(result)
            self.update_display()
        except ZeroDivisionError:
            self.show_error("Cannot divide by zero")
        except Exception:
            self.show_error("Invalid calculation")

    # ----- SCIENTIFIC FUNCTIONS -----
    def get_current_number(self):
        try:
            return float(self.expression)
        except ValueError:
            return None
    def square_root(self):
        number = self.get_current_number()
        if number == None:
            self.show_error("Enter a number first")
            return
        if number < 0:
            self.show_error("Negative numbers can't be used")
            return
        result = math.sqrt(number)
        self.set_result(f"√{number} = {result}", result)
    def sin(self):
        self.trig_function(math.sin, "sin")
    def cos(self):
        self.trig_function(math.cos, "cos")
    def tan(self):
        self.trig_function(math.tan, "tan")
    def asin(self):
        number = self.get_current_number()
        if number == None:
            self.show_error("Enter a number first")
        if not -1 <= number <= 1:
            self.show_error("Value not in range")
        result = math.degrees(math.degrees(math.asin(number)))
        self.set_result(f"arcsin{number} = {result}", result)
    def acos(self):
        number = self.get_current_number()
        if number == None:
            self.show_error("Enter a number first")
        if not -1 <= number <= 1:
            self.show_error("Value not in range")
        result = math.degrees(math.degrees(math.acos(number)))
        self.set_result(f"arccos{number} = {result}", result)
    def atan(self):
        number = self.get_current_number()
        if number == None:
            self.show_error("Enter a number first")
        result = math.degrees(math.degrees(math.atan(number)))
        self.set_result(f"arctan{number} = {result}", result)
    def trig_function(self, function, name):
        number = self.get_current_number()
        if number is None:
            self.show_error("Enter a number first")
            return
        radians = math.radians(number)
        result = function(radians)
        result = round(result, 6)
        self.set_result(f"{name}({number}) = {result}", result)
    def power(self):
        self.add_to_expression("**")

    # ----- HISTORY -----
    def set_result(self, record, result):
        result = round(result, 6)
        self.history.append(record)
        if len(self.history) > 10:
            self.history.pop(0)
        self.last_result = result
        self.expression = str(result)
        self.update_display()
    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Calculation History")
        history_window.geometry("400x400")
        text = tk.Text(
            history_window,
            font=("Arial", 13),
            bg="#202124",
            fg="white"
        )
        text.pack(fill="both", expand=True, padx=10, pady=10)
        if not self.history:
            text.insert(tk.END, "No history yet")
        else:
            for i, calculation in enumerate(self.history, 1):
                text.insert(tk.END, f"{i}. {calculation}\n")
        text.config(state="disabled")

    # ----- ERROR HANDLING -----
    def show_error(self, message):
        self.display.delete(0, tk.END)
        self.display.insert(0, message)
        self.root.after(1500, self.clear)

# ----- MAIN -----
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()