letter = str(input("Add Letter From A to Z : "))

try:
    if (len(letter) >= 2, letter.isalpha() == True):
        print(f"You Typed {letter}")
    else:
        if len(letter) >= 2:
            raise IndexError
        elif letter.isalpha() == False:
            raise TypeError

except TypeError:
    print("The Letter Not In A - Z")
except IndexError:
    print("You Must Write One Character Only")
