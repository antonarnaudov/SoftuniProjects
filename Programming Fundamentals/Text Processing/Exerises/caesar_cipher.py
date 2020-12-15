text = list(input())
encrypted = []
for i in text:
    crypt = ord(i) + 3
    encrypted.append(chr(crypt))
print(''.join(encrypted))
