print("     PYTHON CALCULATOR     ")

num1 = float(input("Enter First Number: "))
operator = (input("Enter Operator (+ - * /): "))
num2 = float(input("Enter Second Number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2


if operator == "+":
    result = addition
elif operator == "-":
    result = subtraction
elif operator == "*":
    result = multiplication
elif operator == "/":
    result = division
    if num2 != 0:
        result = division
    else:
        result = "Cannot be divided by zero"
else:
    result = "Invalid operator"

print(f"Result: {result}")
    