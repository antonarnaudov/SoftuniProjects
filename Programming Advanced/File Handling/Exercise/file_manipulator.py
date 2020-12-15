import os
files_created = set()

while True:
    info = input()
    if info == 'End':
        break
    tokens = info.split('-')
    (command, file_path) = tokens[0], tokens[1]

    if command == 'Create':
        open(file_path, 'w')
        files_created.add(file_path)
        continue

    elif command == 'Add':
        text = tokens[2] + '\n'
        files_created.add(file_path)

        with open(file_path, 'a') as file:
            file.write(text)
        continue

    elif command == 'Replace':
        old_string = tokens[2]
        new_string = tokens[3]

        if file_path in files_created:
            with open(file_path, 'r') as file:
                file_data = file.read()
            file_data = file_data.replace(old_string, new_string)
            with open(file_path, 'w') as file:
                file.write(file_data)
        else:
            print("An error occurred")

    elif command == 'Delete':
        if file_path in files_created:
            os.remove(file_path)
            files_created.remove(file_path)
        else:
            print("An error occurred")
