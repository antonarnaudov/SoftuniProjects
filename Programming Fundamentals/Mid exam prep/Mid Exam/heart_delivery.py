neighborhood = list(map(int, input().split('@')))

start_index = 0

while True:
    tokens = input().split(' ')
    command = tokens[0]
    if command == 'Love!':
        break
    elif command == 'Jump':
        length = int(tokens[1])
        start_index += length

        # result = ((start_index + length) % len(neighborhood))
        if start_index > len(neighborhood) - 1:
            start_index = 0

        # print(start_index)

        neighborhood[start_index] -= 2
        if neighborhood[start_index] == 0:
            print(f"Place {start_index} has Valentine's day.")

        elif neighborhood[start_index] < 0:
            print(f"Place {start_index} already had Valentine's day.")
        # print(neighborhood)

print(f"Cupid's last position was {start_index}.")

failed = 0
for i in neighborhood:
    if i > 0:
        failed += 1

if failed > 0:
    print(f"Cupid has failed {failed} places.")
else:
    print("Mission was successful.")
