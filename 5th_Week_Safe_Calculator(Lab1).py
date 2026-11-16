class InvalidOperationError(Exception):
    pass


while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        operator = input("Enter operator (+, -, *, /): ")

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            result = num1 / num2

        else:
            raise InvalidOperationError("Unsupported operator!")

        print("Result:", result)

    except ValueError:
        print("Error: Invalid numeric input!")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    except InvalidOperationError as e:
        print("Error:", e)

    finally:
        print("Calculation attempt completed.")

    choice = input("Do you want to try again? (yes/no): ")

    if choice.lower() != "yes":
        print("Calculator closed.")
        break