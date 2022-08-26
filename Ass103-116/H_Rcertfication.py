import string
alphabet_string = string.ascii_lowercase
alpha_list = set(alphabet_string)
numbers = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
s = '8hypotheticall024y6wxz'
str_list = [str(z) for z in s]
for i in s:
    if i in numbers:
        numbers.discard(i)


for x in s:
    if x in alpha_list:
        alpha_list.discard(x)
my_s = list(alpha_list)
my_s.sort()
my_n = list(numbers)
my_n.sort()
dd = "".join(my_n)
kk = "".join(my_s)
result = dd+kk
print(result)


# print(str_list)
# for i in str_list:
#     if i in numbers:
#         try:
#             numbers.remove(i)
#         except ValueError:
#             pass
# for char in str_list:
#     if char in alpha_list:
#         try:
#             alpha_list.remove(i)
#         except ValueError:
#             continue

# print(''.join(numbers), end="")
# print(''.join(alpha_list), end="")
