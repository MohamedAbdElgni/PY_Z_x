skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
for countr, skill in enumerate(reversed(list(skills)), 50):
    if type(skill) == int:
        continue
    else:
        print(f"- {countr} - {skill}")
print("*"*50)
new_s = list(skills)
for c, s in enumerate(reversed(new_s), 50):
    if type(s) != str:
        continue
    else:
        print(f"- {c} - {s}")

print("="*50)
indes = 50
for skill in reversed(new_s):
    if type(skill) == int:
        indes += 1
        continue
    else:
        print(f"- {indes} - {skill}")
        indes += 1
