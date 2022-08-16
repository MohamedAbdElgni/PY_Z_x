# 1
num1 = int(input("Enter your num==> ".title()).lstrip().rstrip())
num2 = int(input("Enter your num==> ".title()).lstrip().rstrip())
operation = input(
    r"enter your operatino (+ - * / %) ==>".title()).lstrip().rstrip()
if operation == "+":
    print(f" {num1} {operation} {num2} = {num1+num2}")
elif operation == "-":
    print(f" {num1} {operation} {num2} = {num1-num2}")
elif operation == "*":
    print(f" {num1} {operation} {num2} = {num1*num2}")
elif operation == "%":
    print(f" {num1} {operation} {num2} = {num1%num2}")
elif operation == "/":
    print(f" {num1} {operation} {num2} = {num1/num2}")
print("="*25)
