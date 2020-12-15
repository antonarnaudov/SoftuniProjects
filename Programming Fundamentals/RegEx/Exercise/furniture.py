import re

regex = r'>>([A-Za-z]+)<<(\d+(\.{1}\d+){0,1})!(\d+)'
money = 0
text = input()
print("Bought furniture:")

while text != 'Purchase':
    match = re.match(regex, text)
    if match is None:
        text = input()
        continue

    print(match[1])
    money += float(match[2]) * int(match[4])
    text = input()

print(f"Total money spend: {money:.2f}")
