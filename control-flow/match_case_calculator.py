number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))  
operation = input("Choose an operation(+, -, *, /): ")

match operation:
    case "+":
        result = number1 + number2
        print(f"The result is: {result}")
    case "-":
        result = number1 - number2
        print(f"The result is: {result}")
    case "*":
        result = number1 * number2
        print(f"The result is: {result}")
    case "/":
        if number2 != 0:
            result = number1 / number2
            print(f"The result is: {result}")
        else:
            print("Error: Division by zero is not allowed.")