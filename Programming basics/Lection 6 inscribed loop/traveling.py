destination = input()

while destination != 'End':
    budget_needed = float(input())
    budget_saved = 0
    while budget_needed > budget_saved:
        save = float(input())
        budget_saved += save

    print(f'Going to {destination}!')
    destination = input()

# destination = ''
# budget_saved = 0
# going = True
# while destination != 'End':
#     destination = input()
#     if destination == 'End':
#         destination = 'End'
#         continue
#
#     budget_needed = float(input())
#     while budget_needed > budget_saved:
#         save = float(input())
#         budget_saved += save
#     if going:
#         budget_saved = 0
#         print(f'Going to {destination}!')
