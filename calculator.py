def add(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def power(a, b):
    return a ** b
def remainder(a, b):
    return a % b
def select_op(choice):
    if choice == '$':
        return 0
    if choice == '#':
        return -1
    elif choice in ('+', '-', '*', '^', '/', '%'):
        while True:
            num1 = str(input("Enter first number: "))
            print(num1)
            if num1.endswith("$"):
                return 0
            if num1 .endswith("#"):
                return -1
            num2 = str(input("Enter second number: "))
            print(num2)
            if num2.endswith("$"):
                return 0
            if num2.endswith("#"):
                return -1
            try:
                num1 = float(num1)
                num2 = float(num2)
            except:
                print("Not a valid number,please enter again")
                continue
            while True:
                if choice == '+':
                    print(num1, '+', num2, '=', float(add(num1,num2)))
                    return 0
                elif choice == '-':
                    print(num1, '-', num2, '=', float(substract(num1,num2)))
                    return 0
                elif choice == '*':
                    print(num1, '*', num2, '=', float(multiply(num1, num2)))
                    return 0
                elif choice == '/':
                    if num1 or num2 == 0:
                        print('float division by zero')
                        print(num1, '/', num2, '=', 'None')
                        return 0
                    else:
                        print(num1, '/', num2, '=', float(divide(num1,num2)))
                        return 0
                elif choice == '^':
                    print (num1, '^', num2, '=', float(power(num1, num2)))
                    return 0
                elif choice == '%':
                    print(num1, '%', num2, '=', float(remainder(num1,num2)))
                    return 0
                else:
                    print("Something Went Wrong")
    else:
        print("Unrecognized operation")


while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    if (select_op(choice) == -1):
        # program ends here
        print("Done. Terminating")

    exit()