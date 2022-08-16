# 1
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends[-5])
print(friends[4])
print(friends[-1])
print("="*25)
# 2
print(friends[::2])
print(friends[1::2])
print("="*25)
# 3
print(friends[1:4])
print(friends[-2:])
print("="*25)
# 4
friends[-2:] = ["Elzero", "Elzero"]
print(friends)
print("="*25)
# 5
friends = ["Osama", "Ahmed", "Sayed"]
friends.append("Salem")
print(friends)
friends.insert(0, "Nasser")
print(friends)
print("="*25)
# 6
friends.remove(friends[0])
friends.remove(friends[0])
print(friends)
friends.remove(friends[-1])
print(friends)
print("="*25)
# 7
friends2 = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends2.extend(employees)
friends2.extend(school)
print(friends2)
print("="*25)
# 8
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
print("="*25)
# 9
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0])
print(technologies[-1][-1])
