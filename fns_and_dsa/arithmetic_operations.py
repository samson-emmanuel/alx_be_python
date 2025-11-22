def perform_operation(num1:float, num2:float, operation:str):
    if operation == "subtract":
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
