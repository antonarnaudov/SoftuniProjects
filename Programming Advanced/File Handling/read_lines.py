file = open("08-File-Handling-Lab-Resources/Even Lines/text.txt", 'r')
lines = file.readlines()
[print(line, end="") for line in lines]
print(lines)
print('-' * 80)

for line in lines:
    print(line, end=":NEW:")