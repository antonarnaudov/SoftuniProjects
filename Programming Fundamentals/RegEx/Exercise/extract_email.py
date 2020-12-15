import re

user = r"( |^)[a-z0-9]+([\.\-_][a-z0-9]+)*"
host = r'[a-z]+(-[a-z]+)*(\.[a-z]+(-[a-z]+)*)+'
pattern = rf'{user}@{host}'
text = input()
matches = re.finditer(pattern, text)
for match in matches:
    print(match[0].strip())
