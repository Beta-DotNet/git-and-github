print("Enter either one of the following operations you wish to use: ")
print("+ , - , / , *")
operator = input()

num1 = float(input("Enter Num1: "))
num2 = float(input("Enter Num2: "))

if operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "+":
    result = num1 + num2
elif operator == "/":
    result = num1 / num2
else:
    print("invalid operator!!")