friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_l = []


def text_formatter(text):
    return text[1:-1]


for name in map(text_formatter, friends_map):
    cleaned_l.append(name)
cleaned_l.sort()
for nm in cleaned_l:
    print(f"hello {nm} welcome to our company".title())
print("*"*50)
for name in map(lambda text: f"- {text[1:-1].strip().title()} -", friends_map):
    print(f"welcome {name}".title().center(20, '-'))
