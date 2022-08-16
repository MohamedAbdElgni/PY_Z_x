# 1
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(set(my_list))
print(unique_list)
print(type(unique_list))
print(unique_list[0:len(unique_list)-1])
print("="*25)
# 2
nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums.union(letters))
print(nums | letters)
nums.update(letters)
print(nums)
print("="*25)
# 3
my_set = {1, 2, 3}
print(my_set)
my_set.clear()
print(my_set)
my_set.update("A", "B")
my_set.discard("C")
print(my_set)
print("="*25)
# 4
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_two.issuperset(set_one))
print("="*25)
# 5
my_skills = {"HTML": 90, "CSS": 80, "Python": 30, }
keys = list(my_skills.keys())
print(f"{keys[0]} Progress Is {my_skills.get(keys[0])}%")
print(f"{keys[1]} Progress Is {my_skills.get(keys[1])}%")
print(f"{keys[2]} Progress Is {my_skills.get(keys[2])}%")
my_skills.update({"AI": 20})
keys = list(my_skills.keys())
print(f"{keys[3]} Progress Is {my_skills.get(keys[3])}%")
# print(my_skills)
# print(keys)
