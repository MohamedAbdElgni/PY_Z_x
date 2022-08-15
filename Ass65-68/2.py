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
