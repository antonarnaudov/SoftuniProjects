text = input()
points = 0
for i in text:
    if i == 'a':
        points += 1
    elif i == 'e':
        points += 2
    elif i == 'i':
        points += 3
    elif i == 'o':
        points += 4
    elif i == 'u':
        points += 5
print(points)
