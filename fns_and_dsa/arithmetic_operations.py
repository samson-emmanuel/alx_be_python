def perform_operation(num1, num2, operation):
    if num1 == 0 or num2 == 0:
        print("Error: Cannot perform operations with zero.")
    elif operation == "subtract":
        result = num1 - num2
        print(f'Result: {result}')
    elif operation == "add":
        result = num1 + num2
        print(f'Result: {result}')
    elif operation == "multiply":
        result = num1 * num2
        print(f'Result: {result}')
    elif operation == "divide":
        result = num1 / num2
        print(f'Result: {result}')
    else:
        return "Invalid operation"
    return "Operation performed successfully"