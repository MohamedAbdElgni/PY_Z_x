from logging import exception


NUM = input("enter Your Number==> ".title())
if NUM.isalpha():
    raise exception("Only Numbers allowed")
elif NUM <= "0":
    raise ValueError("ValueError: Number Must Be Larger Than 0")
elif len(NUM) > 1:
    raise IndexError("Only One Character Allowed")
else:
    print("#"*20)
    print("your number is ==> ".title(), NUM)
    print("#"*20)