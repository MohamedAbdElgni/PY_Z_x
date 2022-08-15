def my_s(string):
    for c in reversed(string):
        yield c


x = my_s("elzero".capitalize())
for i in x:
    print(i.capitalize(), end="")
#########################################

print(f'\n{"="*25}')


def reverse_string(my_string):

    yield my_string[::-1]


for c in reverse_string("Elzero"):
    print(c)
