# 1
a = ("mohamed",)

print(a)
print(type(a))
print("="*25)
# 2
friends = ("Osama", "Ahmed", "Sayed")
new_friends = list(friends)
new_friends[0] = "ELzero"
friends = tuple(new_friends)
print(friends)
print(type(friends))
print(len(friends))
print("="*25)
# 3
nums = (1, 2, 3)
letters = ("A", "B", "C")
nums_and_letters_one = nums+letters
print(nums_and_letters_one)
print(len(nums_and_letters_one))
print("="*25)
# 4
my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple
print(f"{a}\n{b}\n{c}")
print("="*25)
