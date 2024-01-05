#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    # Check if the number of arguments is exactly 3 (excluding the script name)
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Assign arguments to variables
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Perform the operation
    if operator == '+':
        print(f"{a} + {b} = {add(a, b)}")
    elif operator == '-':
        print(f"{a} - {b} = {sub(a, b)}")
    elif operator == '*':
        print(f"{a} * {b} = {mul(a, b)}")
    elif operator == '/':
        print(f"{a} / {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
