number1 = float(input("Input a number: "))
operand = input("Type operation: +, -, /, * : ")
number2 = float(input("Input second number: "))

if operand == "+":
    print(number1 + number2)
elif operand == "-":
    print(number1 - number2)
elif operand == "/":
    print(number1 / number2)
elif operand == "*":
    print(number1 * number2)
else:
    print("Invalid Operator")
