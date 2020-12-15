name = str(input())
points_max = 0
winners_name = ''
while name != 'Stop':
    points_counter = 0
    for letters in name:
        correct_answer = ord(letters)
        number = int(input())

        if number == correct_answer:
            points_counter += 10
        else:
            points_counter += 2
    if points_counter > points_max:
        points_max = points_counter
        winners_name = name
    name = input()

print(f"The winner is {winners_name} with {points_max} points!")