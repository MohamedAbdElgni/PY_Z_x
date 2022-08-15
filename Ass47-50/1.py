nums_num = 0

num = int(input("Enter your num:- ".capitalize()))
if num > 0:
    while num > 1:
        num -= 1
        nums_num += 1
        if num == 6:
            continue
        elif num == 0:
            break
        print(num)
    print(f"{nums_num} numbers printed successfully")
else:
    print("your number should be > 0".capitalize().title())
