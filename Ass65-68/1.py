# 1--------------------------------------------------------------
import os
a = 1
while a != 51:
    if a == 25:
        file = open(fr"E:\x\special-text.txt", "w")
    else:
        file = open(fr"E:\x\text{a}.txt", "w")
        file.write(f'Elzero Web School => {a}')
    a += 1
else:
    print(os.getcwd())
    print(os.path.dirname(os.path.abspath(__file__)))
    print(f"{a-1} fils created in x file".title())
file.close()
# 2--------------------------------------------------------------
file = open(fr"E:\x\text1.txt", 'a')
file.write('\nAppended => Elzero Web School'*50)
file.close()
# 3---------------------------------------------------------------
my_file = open(fr"E:\x\text1.txt", "r")
number_lines = 0
number_words = 0
number_chars = 0
for line in my_file:
    line = line.strip("\n")
    line = line.strip(" ")
    word = line.split()
    number_lines += 1
    number_words += len(word)
    number_chars += len(line)
my_file.close()
print(f'{number_lines}\n{number_words}\n{number_chars-(number_words-number_lines)}')
# 4 ---------------------------------------------------------------
count_text = open(fr"E:\x\text1.txt", 'r')
for z in range(41, 51):
    os.remove(fr"E:\x\text{z}.txt")
else:
    print("last 10 files deleted".title())
