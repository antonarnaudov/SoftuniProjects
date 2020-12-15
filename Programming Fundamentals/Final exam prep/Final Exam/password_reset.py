password = input()
args = input()

while args != 'Done':
    args = args.split()
    command = args[0]
    new_password = ''

    if command == 'TakeOdd':
        for i in range(0, len(password)):
            if i == 1 or i % 2 != 0:
                new_password += password[i]
        password = new_password
        print(password)

    elif command == 'Cut':
        index = int(args[1])
        length = int(args[2])
        end = index + length
        password = password.replace(password[index:end], '', 1)
        print(password)

    elif command == 'Substitute':
        substring = args[1]
        substitute = args[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print('Nothing to replace!')

    args = input()

print(f"Your password is: {password}")
