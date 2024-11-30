# Define functions for operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

# Initialize history list
history = []

# Function to display history
def show_history():
    if not history:
        print("No history available.")
    else:
        print("Calculation History:")
        for index, record in enumerate(history, 1):
            print(f"{index}: {record}")

# Main function to handle operations
def select_op(choice):
    if choice == 'H':
        show_history()
        return 1
    if choice == '$':
        return 0
    if choice == '#':
        return -1
    elif choice in ('+', '-', '*', '/', '^', '%'):
        while True:
            num1 = input("Enter first number: ")
            if num1.endswith("$"):
                return 0
            if num1.endswith("#"):
                return -1
            num2 = input("Enter second number: ")
            if num2.endswith("$"):
                return 0
            if num2.endswith("#"):
                return -1
            try:
                num1 = float(num1)
                num2 = float(num2)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            if choice == '+':
                result = add(num1, num2)
            elif choice == '-':
                result = subtract(num1, num2)
            elif choice == '*':
                result = multiply(num1, num2)
            elif choice == '/':
                result = divide(num1, num2)
            elif choice == '^':
                result = power(num1, num2)
            elif choice == '%':
                result = remainder(num1, num2)
            else:
                print("Unrecognized operation.")
                return 1

            # Save to history
            operation = f"{num1} {choice} {num2} = {result}"
            history.append(operation)

            print(operation)
            return 1
    else:
        print("Unrecognized operation.")
        return 1

# Main loop
while True:
    print("Select operation:")
    print("1. Add      : + ")
    print("2. Subtract : - ")
    print("3. Multiply : * ")
    print("4. Divide   : / ")
    print("5. Power    : ^ ")
    print("6. Remainder: % ")
    print("7. History  : H ")
    print("8. Reset    : $ ")
    print("9. Terminate: # ")

    choice = input("Enter choice (+, -, *, /, ^, %, H, $, #): ")
    if select_op(choice) == -1:
        print("Done. Terminating.")
        break
