meals = {}
unlikes = 0

command = input()

while command != 'Stop':
    command = command.split('-')
    guest = command[1]
    meal = command[2]

    if command[0] == 'Like':
        if guest not in meals:
            meals[guest] = [meal]
        elif meal not in meals[guest]:
            meals[guest].append(meal)

    elif command[0] == 'Unlike':
        if guest not in meals:
            print(f"{guest} is not at the party.")
        elif meal not in meals[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            meals[guest].remove(meal)
            unlikes += 1
            print(f"{guest} doesn't like the {meal}.")
    command = input()

sort = dict(sorted(meals.items(), key=lambda x: (-len(x[1]), x[0])))

for key, value in sort.items():
    if len(value) > 0:
        print(f"{key}: ", end="")
        for item in value:
            if item == value[-1]:
                print(item)
                break
            print(item, end=", ")
    else:
        print(f"{key}: ")

print(f"Unliked meals: {unlikes}")
