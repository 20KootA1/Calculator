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
    print("q.  Quit")

    choice = input("Choose an option: ").lower()

    try:
        if choice == "q":
            print("Goodbye!")
            break

        # ---- Unary operations ----
        elif choice in {"6", "7", "8", "9", "10", "11", "12"}:
            num = get_number("Enter number (or 'ans'): ", last_result)

            if choice == "6":
                result = sqrt(num)

            elif choice == "7":
                result = degrees_trig(math.sin, num)

            elif choice == "8":
                result = degrees_trig(math.cos, num)

            elif choice == "9":
                result = degrees_trig(math.tan, num)

            elif choice == "10":
                if not -1 <= num <= 1:
                    raise ValueError("Arcsine input must be between -1 and 1")
                result = math.degrees(math.asin(num))

            elif choice == "11":
                if not -1 <= num <= 1:
                    raise ValueError("Arccosine input must be between -1 and 1")
                result = math.degrees(math.acos(num))

            elif choice == "12":
                result = math.degrees(math.atan(num))

        # ---- Binary operations ----
        else:
            num1 = get_number("First number (or 'ans'): ", last_result)
            num2 = get_number("Second number (or 'ans'): ", last_result)

            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)
            elif choice == "5":
                result = exponent(num1, num2)
            else:
                print("Invalid option.")
                continue

        print("Result:", round(result, 6))
        last_result = result

    except ValueError as e:
        print("Error:", e)
