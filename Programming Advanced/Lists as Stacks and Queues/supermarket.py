from collections import deque


def solve():
    people = deque()

    while True:
        command = input()

        if command == 'End':
            print(f'{len(people)} people remaining.')
            break

        elif command == 'Paid':
            # print customers in queue
            while people:
                print(people.popleft())
        else:
            people.append(command)


solve()
