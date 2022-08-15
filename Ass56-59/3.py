def he_llo(name, *skills):
    if len(skills) == 0:
        print(f"hello {name} you have no skills to show...".title())
    else:
        print(f"hello {name} your skills is --->".title())
        for skill in skills:
            print(skill)


he_llo("Osama", "HTML", "CSS", "JS", "Python")
he_llo("ahmed")
