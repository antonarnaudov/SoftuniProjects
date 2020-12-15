register = {}
while True:
    tokens = input()
    if tokens == 'Statistics':
        break
    tokens = tokens.split('->')
    command = tokens[0]
    username = tokens[1]

    if command == 'Add':
        if username in register:
            print(f"{username} is already registered")
            continue
        else:
            register[username] = []

    elif command == 'Send':
        email = tokens[2]
        if email not in register[username]:
            register[username].append(email)

    elif command == 'Delete':
        if username not in register:
            print(f"{username} not found!")
            continue
        register.pop(username)

register = dict(sorted(register.items(), key=lambda u: (-len(u[1]), u[0])))

print(f'Users count: {len(register)}')
for users, emails in register.items():
    print(users)
    for email in emails:
        print(f' - {email}')
