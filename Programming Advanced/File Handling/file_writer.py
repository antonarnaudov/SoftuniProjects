path = '08-File-Handling-Lab-Resources/my_first_file.txt'
with open(path, 'w') as file:
    file.write('I just created my first file!')

with open(path, 'r') as file:
    print(file.read())
