# Basic calculator program

# ask for user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# perform calculations
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by Zero."
else:
    result = "Invalid operation"

# Display result
if isinstance(result, (int, float)):
    print(
        f"The result of: {int(num1)} {operation} {int(num2)} is equal to: {int(result)}"
    )
else:
    print(f"Result is: {result}")
