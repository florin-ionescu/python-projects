# Basic Calculator App

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return ("Cannot divide by zero")
    else:
        return a/b

def square(a, b):
    return a**b

def floor_division(a,b):
    return a//b

def remainder(a,b):
    return a%b

def calculator():
    while True:
        print("\nCalculator App Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square")
        print("6. Floor Division")
        print("7. Remainder")
        print("8. Exit\n")

        choice = input("Choose an option from the menu: ")

        if choice =="8":
            print("Calculator App Powered Off.")
            break

        if choice not in ["1","2","3","4","5","6","7","8"]:
            print("Invalid option. You must type a number between 1 and 8.")
            continue

        try:
            num1 = float(input("Please enter a number: "))
            num2 = float(input("Please enter a second number: "))
        except ValueError:
            print("Please enter a valid number.")
        if choice == "1":
            result = add(num1,num2)
            print("Result:", result)
        elif choice == "2":
            result = subtract(num1,num2)
            print("Result:", result)
        elif choice == "3":
            result = multiply(num1,num2)
            print("Result:", result)
        elif choice == "4":
            result = divide(num1,num2)
            print("Result:", result)
        elif choice == "5":
            result = square(num1,num2)
            print("Result:", result)
        elif choice == "6":
            result = floor_division(num1,num2)
            print("Result:", result)
        elif choice == "7":
            result = remainder(num1,num2)
            print("Result:", result)

calculator()