scores = {"math": 90, "sinence": 80, "Language": 70}


def get_people_scores(*name, **skills):
    if len(name) == 0:
        for key, value in skills.items():
            print(f"{key}---> {value}".title())
    elif len(skills) == 0:
        for name1 in name:
            print(f"Hello {name1} You Have No Scores To Show".title())
    else:
        for name1 in name:
            print(f"hello {name1} this is your score table:-->".title())
        for key, value in skills.items():
            print(f"{key}---> {value}".title())


get_people_scores("osama", **scores)
print("*"*35)
get_people_scores("Osama")
print("*"*35)
get_people_scores(**scores)
