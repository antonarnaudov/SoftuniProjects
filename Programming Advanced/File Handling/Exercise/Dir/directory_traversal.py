import os

path = input()
sep_count = path.count(os.path.sep)
dictionary = {}

for root, dirs, files in os.walk(path):
    if sep_count - root.count(os.path.sep) > 1:
        continue

    for file in files:
        extension = file.split('.')[-1]
        if extension not in dictionary:
            dictionary[extension] = []
        dictionary[extension].append(file)
        # print(file)

# print(sorted(dictionary))
result_str = ''

for key, value in sorted(dictionary.items()):
    result_str += f'.{key}\n'
    for file in sorted(value):
        result_str += f'- - - {file}\n'
print(result_str)

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
final_location = desktop + os.path.sep + 'report.txt'

with open(final_location, 'w') as file:
    file. write(result_str)
