import datetime

start = datetime.datetime.now()
text = input()

for i in range(0, len(text)):
    if text[i] == ":":
        if text[i + 1] != " ":
            print(f":{text[i + 1]}")
finish = datetime.datetime.now()
# 0:00:01.328140

# text = input()
# dictionary = {':': []}
# emoji = False
# for letter in text:
#     if emoji:
#         dictionary[':'].append(letter)
#
#     emoji = False
#     if letter == ':':
#         emoji = True
#         continue
# for i in range(0, len(dictionary[':'])):
#     print(':' + dictionary[':'][i])
# finish = datetime.datetime.now()
# 0:00:02.254866
print(finish - start)
