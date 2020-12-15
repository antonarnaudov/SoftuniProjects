from collections import deque


def list_manipulator(number_ll, command, place, *args):
    number_ll = deque(number_ll)

    if command == 'add' and place == 'beginning':
        for x in reversed(args):
            number_ll.appendleft(x)
        return list(number_ll)

    elif command == 'add' and place == 'end':
        for x in args:
            number_ll.append(x)
        return list(number_ll)

    elif command == 'remove' and place == 'beginning':
        if args:
            for x in args:
                for _ in range(x):
                    number_ll.popleft()
        else:
            number_ll.popleft()
        return list(number_ll)

    elif command == 'remove' and place == 'end':
        if args:
            for x in args:
                for _ in range(x):
                    number_ll.pop()
        else:
            number_ll.pop()
        return list(number_ll)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
