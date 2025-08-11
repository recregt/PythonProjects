def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("Select an operation: +, -, *, /")
        operation = input("Enter your choice: ")

        if operation == '+':
            print(add(num1, num2))
        elif operation == '-':
            print(subtract(num1, num2))
        elif operation == '*':
            print(multiply(num1, num2))
        elif operation == '/':
            print(divide(num1, num2))
        else:
            print("Invalid operation.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")