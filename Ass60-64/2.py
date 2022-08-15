# you can do it like this also ---->  def get_people scores(name="" ,**skills): # --to limit the high usage of for loops
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


get_people_scores("Osama", Math=90, Science=80, Language=70)
print("#"*30)
get_people_scores("Mahmoud", Logic=70, Problems=60)
print("#"*30)
get_people_scores(Logic=70, Problems=60)
print("#"*30)
get_people_scores("Ahmed")
