import re

text = input()  # .lower()
r = input()  # .lower()
regex = fr"\b{r}\b"
result = re.findall(regex, text, re.IGNORECASE)
print(len(result))
