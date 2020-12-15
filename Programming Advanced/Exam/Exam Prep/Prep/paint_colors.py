def find_middle(string):
    return len(string) // 2


text = input().split()
colors = []

main_colors = ['red', 'yellow', 'blue']
secondary_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

while text:
    first_element = text.pop(0)
    last_element = text.pop() if text else ''

    word = first_element + last_element
    reversed_word = last_element + first_element

    if word in main_colors \
            or word in secondary_colors:
        colors.append(word)

    elif reversed_word in main_colors \
            or reversed_word in secondary_colors:
        colors.append(reversed_word)

    else:
        first_element = first_element[:-1]
        last_element = last_element[:-1]

        if first_element:
            text.insert(find_middle(text), first_element)

        if last_element:
            text.insert(find_middle(text), last_element)

for color in colors:
    if secondary_colors.get(color):
        # if any(c for c in secondary_colors[color] if c not in colors):
        if any(x not in colors for x in secondary_colors[color]):
            colors.remove(color)
            del secondary_colors[color]

print(colors)
