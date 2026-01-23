import math

def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def exponent(x,y):
   return x ** y
def sqrt(x):
   return math.sqrt(x)

calculate = ("True")
while calculate == "True":

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
    choice = str(input("Choose: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12: "))

    if choice == "6" or choice == "7" or choice == "8" or choice == "9" or choice == "10" or choice == "11" or choice == "12":
        num = float(input("Select the number: "))
    else:
        num1 = float(input("Select the first number: "))
        num2 = float(input("Select the second number: "))

    if choice == "1":
        ans = (add(num1,num2))
        print(ans)
    elif choice == "2":
        ans = (subtract(num1,num2))
        print(ans)
    elif choice == "3":
        ans = (multiply(num1,num2))
        print(ans)
    elif choice == "4":
        ans = (divide(num1,num2))
        print(ans)
    elif choice == "5":
        ans = (exponent(num1,num2))
        print(ans)
    elif choice == "6":
        ans = (math.sqrt(num))
        print(ans)
    elif choice == "7":
        print(math.sin(math.radians(num)))
    elif choice == "8":
        print(math.cos(math.radians(num)))
    elif choice == "9":
        print(math.tan(math.radians(num)))
    elif choice == "10":
        radians_result = math.asin(num)
        degrees_result = math.degrees(radians_result)
        print(degrees_result)
    elif choice == "11":
        radians_result = math.acos(num)
        degrees_result = math.degrees(radians_result)
        print(degrees_result)
    elif choice == "12":
        radians_result = math.atan(num)
        degrees_result = math.degrees(radians_result)
        print(degrees_result)
    cont = input("Would you like to do another calculation? (y/n): ")
    if cont == "y":
       calculate = ("True")
    elif cont == "n":
       calculate = ("False")
