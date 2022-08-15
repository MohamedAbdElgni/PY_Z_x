def calculate():
    i = []
    max_num = int(input("how many nums you wanna calculate--> ".title()))
    while max_num > 0:
        u_num = int(input("Enter your number--> ".title()))
        max_num -= 1
        if u_num == 10:
            continue
        i.append(u_num)

    else:
        if 5 in i:
            print(sum(i)-10)
        else:
            print(sum(i))
        print("Function is Done".title())


calculate()

#--------------------------------------------------------------#
#---------------------Another method---------------------------#
#--------------------------------------------------------------#


def addition(*n):
    ig = 0
    for n2 in n:
        if n2 == 5:
            ig -= 10
        elif n2 == 10:
            ig -= 10
    print(sum(n)+ig)


addition(10, 20, 30, 10, 15)
addition(10, 20, 30, 10, 15, 5, 100)
