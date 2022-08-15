my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
for i1, i2 in zip(my_list, my_tuple):
    print(f"{i1}{i2}".strip(), end="")
