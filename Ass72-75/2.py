friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
for names in filter(lambda name: name[-1] == "m", friends_filter):
    print(names.title().strip().center(20, '-'))
print('#'*50)


def tx(text):
    return text[-1] == "m"


n_l = filter(tx, friends_filter)
for name in n_l:
    print(name)
