# # list with dublicated elements
from collections import Counter as C
# my_list = ["bcdef", "abcdefg", "bcde", "bcdef"]
# my_set = set(my_list)
# my_clean_list = list(my_set)
# d_valu = Counter(my_list)
# x = 0
# for v in my_clean_list:
#     print(d_valu[v], end=" ")
# # ===================================
# n = int(input())
# my_list = []
# order = []

# while n > 0:
#     iword = input()
#     my_list.append(iword)
#     n -= 1

# myset = set(my_list)
# my_clean_list = list(myset)
# d_valu = Counter(my_list)
# print(len(my_clean_list))
# for v in my_clean_list:
#     order.append(d_valu[v])
# print((order))
my_list = [0, 0, 1, 2, 2, 3, 3, 4, 4]
my_empty_list = set(my_list)
C_list = C(my_list)
print(len(my_empty_list))

print(f"{x}" for x in C_list.values())
