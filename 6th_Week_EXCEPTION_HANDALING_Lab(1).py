class InvalidOperationError(Exception):
    pass

while True:
    try:
        num1_input = input("Enter first number (or 'exit' to quit): ")
        if num1_input.lower() == 'exit':
            break
        num1 = float(num1_input)

        num2_input = input("Enter second number: ")
        num2 = float(num2_input)

        operator = input("Enter an operation (+, -, *, /): ")

        if operator not in ['+', '-', '*', '/']:
            raise InvalidOperationError(f"Operator '{operator}' is not supported.")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2

        print(f"Result: {result}")

    except ValueError:
        print("Error: Invalid numeric input. Please enter valid numbers.")
    except InvalidOperationError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    finally:
        print("Calculation attempt completed.")
