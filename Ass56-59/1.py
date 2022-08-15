def a_sking():
    ask = str(input("you wanna try angain(y-n)".title()))
    if ask == "Y" or ask == "y" or ask == "yes":
        calculator()
    else:
        print("closing calculator\ndone\nsee you later".title())


def calculator():
    n1 = int(input("enter your first num :---> ".title()))
    n2 = int(input("enter your secound num :---> ".title()))
    sign = str(input("enter your sign (Add-Sub-Multiply)---> ".title()))
    if sign == "A" or sign == "a" or sign == "add" or sign == "+" or sign == "":
        print(n1+n2)
        a_sking()
    elif sign == "s" or sign == "S" or sign == "sub" or sign == "-":
        print(n1-n2)
        a_sking()

    elif sign == "M" or sign == "m" or sign == "multiply" or sign == "*":
        print(n1*n2)
        a_sking()

    else:
        print(f"wrong operator\ngoodby".title())


calculator()
#--------------------------------------------------------------#
#---------------------Another method---------------------------#
#--------------------------------------------------------------#


def calculate(n1, n2, sign="multiply"):
    if sign.lower() == "add" or sign == "a":
        print(n1 + n2)
    elif sign.lower() == "subtract" or sign == "s":
        print(n1 - n2)
    elif sign.lower() == "multiply" or sign == "m":
        print(n1 * n2)
    else:
        print("The Operation Is Wrong")


calculate(10, 20, "m")
