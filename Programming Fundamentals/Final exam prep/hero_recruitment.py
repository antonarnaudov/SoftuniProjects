collection = {}  # {hero: [spellbook]}
command = input()
while command != 'End':
    tokens = command.split()
    command = tokens[0]
    hero_name = tokens[1]
    
    if command == 'Enroll':
        if hero_name in collection:
            print(f"{hero_name} is already enrolled.")
        else:
            collection[hero_name] = []
        command = input()
        continue

    spell_name = tokens[2]
    if command == 'Learn':
        if hero_name not in collection:
            print(f"{hero_name} doesn't exist.")
        elif spell_name in collection[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            collection[hero_name].append(spell_name)
    elif command == 'Unlearn':
        if hero_name not in collection:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in collection[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            collection[hero_name].remove(spell_name)
    command = input()

sort = dict(sorted(collection.items(), key=lambda x: (-len(x[1]), x[0])))
print(f'Heroes:')

for key, value in sort.items():
    if len(value) > 0:
        print(f"== {key}: ", end="")
        for item in value:
            if item == value[-1]:
                print(item)
                break
            print(item, end=", ")
    else:
        print(f"== {key}: ")
