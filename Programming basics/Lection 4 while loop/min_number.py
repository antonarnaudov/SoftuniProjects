numbers_count = int(input())

counter = 1
smallest_number = 0
while counter <= numbers_count:
    current_number = int(input())
    if counter == 1:
        #print('Stored first number')
        smallest_number = current_number

    elif current_number <= smallest_number:
        smallest_number = current_number

    counter += 1

print(smallest_number)