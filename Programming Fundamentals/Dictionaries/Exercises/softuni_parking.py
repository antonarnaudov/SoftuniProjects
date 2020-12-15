number = int(input())
registered = {}
for i in range(number):
    token = input().split()
    command = token[0]
    username = token[1]
    if command == 'register':
        license_plate = token[2]
        if username not in registered:
            registered[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif command == 'unregister':
        if username not in registered:
            print(f"ERROR: {username} not found")
        else:
            registered.pop(username)
            print(f"{username} unregistered successfully")
for x, y in registered.items():
    print(f'{x} => {y}')
