def my_all(i):
    index = 0
    for x in i:
        if bool(x) == True:
            index += 1
    if len(i) == index:
        return"True"
    else:
        return"false"


print(my_all([1, 2, 3]))
print(my_all([1, 2, 3, []]))
print("*"*50)


def my_any(v):
    for z in v:
        if bool(z) == True:
            return True
    return False


print(my_any([0, 1, [], False]))
print(my_any([(), 0, False]))
print("*"*50)


def my_min(var):
    l_i = list(var)
    l_i.sort()
    return l_i[0]


print(my_min([10, 100, -20, -100, 50]))  # -100
print(my_min((10, 100, -20, -100, 50)))  # -100
print("*"*50)


def my_max(var):
    l_i = list(var)
    l_i.sort(reverse=True)
    return l_i[0]


print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 700)))  # 700
