from functools import reduce
nums = [2, 4, 6, 2]


def darb(num1, num2):
    return num1*num2


n_num = reduce(darb, nums)
print(n_num)


print('='*50)

print(reduce(lambda x1, x2: x1*x2, nums))
