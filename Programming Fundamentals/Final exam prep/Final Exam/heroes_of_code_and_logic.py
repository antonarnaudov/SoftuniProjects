number = int(input())
health = {}
mana = {}

for _ in range(number):
    args = input().split()

    hero = args[0]
    hp = int(args[1])
    mn = int(args[2])

    health[hero] = hp
    mana[hero] = mn

args = input()
while args != 'End':
    out_of_range = 0
    args = args.split(' - ')
    command = args[0]
    hero = args[1]

    if command == 'CastSpell':
        mp_needed = int(args[2])
        spell_name = args[3]
        if mana[hero] >= mp_needed:
            mana[hero] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {mana[hero]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif command == 'TakeDamage':
        damage = int(args[2])
        attacker = args[3]
        if health[hero] - damage > 0:
            health[hero] -= damage
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {health[hero]} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            del health[hero]
            del mana[hero]

    elif command == 'Recharge':
        amount = int(args[2])

        if mana[hero] + amount > 200:
            out_of_range = 200 - mana[hero]
            mana[hero] = 200
            print(f"{hero} recharged for {out_of_range} MP!")
        else:
            mana[hero] += amount
            print(f"{hero} recharged for {amount} MP!")

    elif command == 'Heal':
        amount = int(args[2])
        if health[hero] + amount > 100:
            out_of_range = 100 - health[hero]
            health[hero] = 100
            print(f"{hero} healed for {out_of_range} HP!")
        else:
            health[hero] += amount
            print(f"{hero} healed for {amount} HP!")

    args = input()

sort = dict(sorted(health.items(), key=lambda x: (-x[1], x[0])))

for key, value in sort.items():
    print(key)
    print(f"HP: {value}")
    print(f"MP: {mana[key]}")
