import re

r = r'(w{3}\.[a-zA-Z0-9\-]+(\.[a-z]+)+)'
text = input()
while text != '':
    match = [x[0] for x in re.findall(r, text)]
    for m in match:
        print(m)
    text = input()
