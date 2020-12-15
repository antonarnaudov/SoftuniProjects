path = '08-File-Handling-Lab-Resources/File Reader/numbers.txt'
file = open(path, 'r')

num_sum = 0
for num in file:
    num_sum += int(num)
    print(num)  # read

print(num_sum)
print(file.read())  # .read(n) n = number
