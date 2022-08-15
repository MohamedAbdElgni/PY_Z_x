def get_score(**Skills):
    for kEy, value in Skills.items():
        print(f"{kEy} ----> {value}")


get_score(Math=90, Science=80, Language=70)
print("#"*30)
get_score(Logic=70, Problems=60)
