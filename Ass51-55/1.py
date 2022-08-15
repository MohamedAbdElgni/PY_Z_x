my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)
for n_m in my_nums:
    if n_m % 5 == 0:

        print(n_m)
else:
    print("Loop is Done")
