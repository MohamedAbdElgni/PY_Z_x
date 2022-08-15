friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
counter = 0
friends.sort()
while counter > -1:
    if friends[counter].islower() == True:
        break
    print(f"{friends[counter]}")
    counter += 1

print(f"Friends Printed And Ignored Names Count Is {len(friends)-counter}")
