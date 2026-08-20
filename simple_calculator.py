def calculator():
    print("Simple Calculator")
    print("Enter two numbers and choose an operation.")

    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    op = input("Enter +, -, *, or /: ")

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("Cannot divide by zero.")
            return
        result = a / b
    else:
        print("Unknown operation.")
        return

    print("Result:", result)


if __name__ == "__main__":
    calculator()


