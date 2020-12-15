email = input()
while True:
    command = input()
    if command == 'Complete':
        break
    tokens = command.split()
    command = tokens[0]
    if command == 'Make':
        command = tokens[1]
        if command == 'Upper':
            email = email.upper()
            print(email)
        elif command == 'Lower':
            email = email.lower()
            print(email)

    elif command == 'GetDomain':
        count = int(tokens[1])
        print(email[-count:])

    elif command == 'GetUsername':
        if '@' in email:
            index = email.index('@')
            print(email[:index])
        else:
            print(f"The email {email} doesn't contain the @ symbol.")

    elif command == 'Replace':
        char = tokens[1]

        email = email.replace(char, '-')
        print(email)

    elif command == 'Encrypt':
        for i in email:
            print(f'{ord(i)}', end=" ")
