text = input()
final_text = ''
appended = ''

for i in range(0, len(text)):
    if text[i] != appended:
        final_text += text[i]
        appended = text[i]
print(final_text)
