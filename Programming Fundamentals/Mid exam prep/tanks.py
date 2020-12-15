collection = input().split(', ')

count = int(input())
counter = 0
while count != counter:
    a = input().split(', ')
    command = a[0]
    if command == 'Add':
        tank_name = a[1]
        if tank_name in collection:
            print("Tank is already bought")
        else:
            print('Tank successfully bought')
            collection.append(tank_name)

    elif command == 'Remove':
        tank_name = a[1]
        if tank_name in collection:
            print("Tank successfully sold")
            collection.remove(tank_name)
        else:
            print('Tank not found')

    elif command == 'Remove At':
        index = int(a[1])
        if len(collection) >= index:
            collection.remove(collection[index])
            print('Tank successfully sold')
        else:
            print("Index out of range")

    elif command == 'Insert':
        index = int(a[1])
        tank_name = a[2]

        if len(collection) >= index:
            if tank_name not in collection:
                collection.insert(index, tank_name)
                print('Tank successfully bought')
            else:
                print('Tank already bought')
        else:
            print("Index out of range")
    counter += 1
print(', '.join(collection))
