num_lines = int(input())
counter = 0
result = 0
while num_lines > counter:
    letter = input()
    result += ord(letter)
    counter += 1
print(f'The sum equals: {result}')
