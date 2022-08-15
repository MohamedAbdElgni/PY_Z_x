import pyfiglet
import termcolor
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []
for i1, i2, i3 in zip(my_list1, my_tuple, my_list2):
    if type(i2) == int:
        break
    if type(i3) == int:
        break
    else:

        my_data.append(i2)
        my_data.append(i3)

print(termcolor.colored(pyfiglet.figlet_format(
    "".join(my_data).capitalize(), width=100), color="cyan"))


print(termcolor.colored(pyfiglet.figlet_format(
    "that's a hard one".title(), font="digital", width=100), color="cyan"))
