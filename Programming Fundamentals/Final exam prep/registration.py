import re
n = int(input())
counter = 0
regex = r"U\$([A-Z]{1}[a-z]{2,})U\$P@\$([A-Za-z]{5,}\d+)P@\$"

for _ in range(n):
    text = input()
    match = re.match(regex, text)
    if match is None:
        print("Invalid username or password")
        continue
    print("Registration was successful")
    print(f'Username: {match[1]}, Password: {match[2]}')
    counter += 1
print(f'Successful registrations: {counter}')

# if re.match(regex, text):
#     text = text.split('$P')
#     username = text[0].strip('U').strip('$')
#     password = text[1].strip('@$').strip('P')
#     print("Registration was successful")
#     print(f"Username: {username}, Password: {password}")
#     counter += 1
# else:
#     print("Invalid username or password")
