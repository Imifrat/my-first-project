def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Simple command-line calculator")
    parser.add_argument("operation", choices=OPERATIONS, help="Operation to perform")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    args = parser.parse_args()

    try:
        result = OPERATIONS[args.operation](args.a, args.b)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
        raise SystemExit(1)

if __name__ == "__main__":
    main()
