"""Simple command-line calculator"""

def add(x, y):
    """Return the sum of x and y."""
    return x + y


def subtract(x, y):
    """Return the difference of x and y."""
    return x - y


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


def divide(x, y):
    """Return the division of x by y. Raises ValueError on division by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def main():
    """Run a simple interactive calculator loop."""
    print("Simple calculator. Type 'q' to exit.")
    while True:
        op = input("Operation (+, -, *, /): ").strip()
        if op.lower() == 'q':
            break
        if op not in {"+", "-", "*", "/"}:
            print("Invalid operation")
            continue
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
        except ValueError:
            print("Invalid number")
            continue
        try:
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            else:
                result = divide(num1, num2)
        except ValueError as exc:
            print(exc)
        else:
            print(f"Result: {result}")


if __name__ == "__main__":
    main()
