# Simple Calculator

A Python-based command-line calculator that performs basic arithmetic operations with error handling and user-friendly controls.

## Features
- Supports the following operations:
  - **Addition (`+`)**: Add two numbers.
  - **Subtraction (`-`)**: Subtract one number from another.
  - **Multiplication (`*`)**: Multiply two numbers.
  - **Division (`/`)**: Divide one number by another with a check to avoid division by zero.
  - **Power (`^`)**: Raise one number to the power of another.
  - **Remainder (`%`)**: Calculate the remainder of division.
- Includes special commands:
  - **Reset (`$`)**: Reset the program to start over.
  - **Terminate (`#`)**: Exit the program gracefully.
- Handles invalid inputs with appropriate error messages.
- Prevents division by zero with a detailed warning.

## How to Use
1. **Run the script**:
   - Open a terminal and execute:
     ```bash
     python calculator.py
     ```
2. **Follow the on-screen instructions**:
   - Enter an operation symbol (e.g., `+`, `-`, `*`, `/`, `^`, `%`).
   - Provide the two numbers when prompted.
   - Use `$` to reset the program or `#` to terminate.

3. **Example Output**:
   Select operation.
   Select operation.
   Select operation.
   1.Add      : + 
   2.Subtract : - 
   3.Multiply : * 
   4.Divide   : / 
   5.Power    : ^ 
   6.Remainder: % 
   7.Terminate: # 
   8.Reset    : $ 
   Enter choice(+,-,*,/,^,%,#,$): +
   Enter first number: 2
   Enter second number: 4
   2.0 + 4.0 = 6.0
