Lett = str(input("Add Letter From A to Z==> "))
try:
    if len(Lett) == 1 and Lett.isalpha() == True:
        print(f"You Typed {Lett}")
    else:
        if len(Lett) > 1:
            raise IndexError
        elif Lett.isalpha() == False:
            raise TypeError

except IndexError:
    print("You Must Write One Character Only")
except TypeError:
    print("The Letter Not In A - Z")
