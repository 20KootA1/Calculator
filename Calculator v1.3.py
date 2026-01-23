import math


# ---- Basic operations ----
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def exponent(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(x)


# ---- Input handling ----
def get_number(prompt, last_result):
    while True:
        user_input = input(prompt).lower()

        if user_input == "ans":
            if last_result is None:
                print("No previous result available.")
            else:
                return last_result
        else:
            try:
                return float(user_input)
            except ValueError:
                print("Please enter a valid number or 'ans'.")


def degrees_trig(func, value):
    return func(math.radians(value))


# ---- Main program ----
last_result = None
history = []

while True:
    print("\nCalculator Menu")
    print("1.  Addition")
    print("2.  Subtraction")
    print("3.  Multiplication")
    print("4.  Division")
    print("5.  Exponential")
    print("6.  Square Root")
    print("7.  Sine")
    print("8.  Cosine")
    print("9.  Tangent")
    print("10. Arcsine")
    print("11. Arccosine")
    print("12. Arctangent")
    print("h.  View History")
    print("q.  Quit")

    choice = input("Choose an option: ").lower()

    try:
        if choice == "q":
            print("Goodbye!")
            break

        elif choice == "h":
            if not history:
                print("No history yet.")
            else:
                print("\nCalculation History:")
                for i, entry in enumerate(history, start=1):
                    print(f"{i}) {entry}"
            continue

        # ---- Single Unit Operations ----
        elif choice in {"6", "7", "8", "9", "10", "11", "12"}:
            num = get_number("Enter number (or 'ans'): ", last_result)

            if choice == "6":
                result = sqrt(num)
                record = f"sqrt({num}) = {result}"

            elif choice == "7":
                result = degrees_trig(math.sin, num)
                record = f"sin({num}) = {result}"

            elif choice == "8":
                result = degrees_trig(math.cos, num)
                record = f"cos({num}) = {result}"

            elif choice == "9":
                result = degrees_trig(math.tan, num)
                record = f"tan({num}) = {result}"

            elif choice == "10":
                if not -1 <= num <= 1:
                    raise ValueError("Arcsine input must be between -1 and 1")
                result = math.degrees(math.asin(num))
                record = f"asin({num}) = {result}"

            elif choice == "11":
                if not -1 <= num <= 1:
                    raise ValueError("Arccosine input must be between -1 and 1")
                result = math.degrees(math.acos(num))
                record = f"acos({num}) = {result}"

            elif choice == "12":
                result = math.degrees(math.atan(num))
                record = f"atan({num}) = {result}"

        # ---- Double Unit Operations ----
        else:
            num1 = get_number("First number (or 'ans'): ", last_result)
            num2 = get_number("Second number (or 'ans'): ", last_result)

            if choice == "1":
                result = add(num1, num2)
                record = f"{num1} + {num2} = {result}"

            elif choice == "2":
                result = subtract(num1, num2)
                record = f"{num1} - {num2} = {result}"

            elif choice == "3":
                result = multiply(num1, num2)
                record = f"{num1} * {num2} = {result}"

            elif choice == "4":
                result = divide(num1, num2)
                record = f"{num1} / {num2} = {result}"

            elif choice == "5":
                result = exponent(num1, num2)
                record = f"{num1} ** {num2} = {result}"

            else:
                print("Invalid option.")
                continue

        # ---- Save result ----
        result = round(result, 6)
        print("Result:", result)

        last_result = result
        history.append(record)

        if len(history) > 10:
            history.pop(0)

    except ValueError as e:
        print("Error:", e)
