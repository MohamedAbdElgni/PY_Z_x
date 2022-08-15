my_l = ['mohamed', 'ahmed', 'ali', 'omer']
for num, name in enumerate(my_l):
    if name == "mohamed":
        continue

    else:
        print(f"- {num+1} - {name.capitalize()}")
