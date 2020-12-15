experience_needed = float(input())
battles_count = int(input())

experience_sum = 0
ready = False
for battle in range(1, battles_count + 1):
    experience_per_battle = float(input())
    if battle % 3 == 0:
        experience_sum += experience_per_battle + (experience_per_battle * 0.15)
    elif battle % 5 == 0:
        experience_sum += experience_per_battle - (experience_per_battle * 0.1)
    else:
        experience_sum += experience_per_battle
    if experience_sum >= experience_needed:
        battles_count = battle
        ready = True
        break

if ready:
    print(f"Player successfully collected his needed experience for {battles_count} battles.")
else:
    needed = experience_needed - experience_sum
    print(f"Player was not able to collect the needed experience, {needed:.2f} more needed.")
