my_friends = []
maxfriends = 5

while maxfriends > 0:
    name = input("Please Enter Your Name :-> ").strip()
    if name.isupper():
        print("Invalid Name")
    elif name.islower():
        name.capitalize()
        my_friends.append(name.capitalize())
        maxfriends -= 1
        print(f"Friend {name.capitalize()} Added => 1st Letter Become Capital")
        print(f"Names Left in List Is {maxfriends}")
    else:
        my_friends.append(name)
        maxfriends -= 1
        print(f"Friend {name} Added")
        print(f"Names Left in List Is {maxfriends}")
else:
    print("Names List Is Full , You Cant Add more")
if len(my_friends) > 0:
    my_friends.sort()
    index = 0
    print("Printing The List Of Names")

    while index < len(my_friends):
        print(my_friends[index])
        index += 1
