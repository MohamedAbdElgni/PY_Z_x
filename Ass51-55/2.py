for i in range(1, 21):
    if i == 6 or i == 8 or i == 12:
        continue
    elif i < 10:
        print(f"0{i}")
    else:
        print(i)
else:
    print("all numbers printed".title())
