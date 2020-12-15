def valid():
    return bomb_types['Datura Bombs'] >= 3 \
           and bomb_types['Cherry Bombs'] >= 3 \
           and bomb_types['Smoke Decoy Bombs'] >= 3


bomb_effects = [int(x) for x in input().split(', ')]
bomb_castings = [int(x) for x in input().split(', ')]

materials = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs'
}

bomb_types = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}
while True:
    if not bomb_effects:
        break
    elif not bomb_castings:
        break
    elif valid():
        break

    current_sum = bomb_effects[0] + bomb_castings[-1]

    if current_sum in materials.keys():
        for key, value in materials.items():
            if current_sum == key:
                bomb_types[value] += 1
                bomb_effects.pop(0)
                bomb_castings.pop()
    else:
        bomb_castings[-1] -= 5

if 3 in bomb_types.values():
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print('Bomb Effects: empty')

if bomb_castings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_castings])}")
else:
    print('Bomb Casings: empty')

sort = dict(sorted(bomb_types.items()))
for key, value in sort.items():
    print(f"{key}: {value}")
