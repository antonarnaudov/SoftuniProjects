lost_games = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

summary = 0

for game in range(1, lost_games + 1):

    if game % 2 == 0:
        summary += helmet_price
    if game % 3 == 0:
        summary += sword_price
    if game % 6 == 0:
        summary += shield_price
    if game % 12 == 0:
        summary += armor_price
print(f'"Gladiator expenses: {summary} aureus"')