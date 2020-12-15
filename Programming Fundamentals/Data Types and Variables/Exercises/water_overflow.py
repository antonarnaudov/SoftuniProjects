num_lines = int(input())
limit = 255
counter = 0
line_counter = 0
while counter < num_lines:
    line = int(input())
    line_counter += line
    if line_counter > limit:
        line_counter -= line
        print('Insufficient capacity!')
    counter += 1
print(line_counter)