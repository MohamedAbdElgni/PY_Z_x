def list_to_string(s_l):
    str1 = ""

    return str1.join(s_l)


my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple2 = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data2 = []
for item1, item2, item3 in zip(my_list1, my_tuple2, my_list2):
    if isinstance(item2, int) is True:
        break
    if isinstance(item3, int) is True:
        break
    my_data2.append(item2)
    my_data2.append(item3)

FINALL_STRING = list_to_string(my_data2).capitalize()
print(my_data2)


print(FINALL_STRING)
