passengers_count = int(input())
stops_count = int(input())

stops_counter = 0
passengers_counter = passengers_count

while stops_count > stops_counter:
    down = int(input())
    passengers_counter -= down
    up = int(input())
    passengers_counter += up
    stops_counter += 1
    if stops_counter % 2 == 0:
        passengers_counter -= 2
    else:
        passengers_counter += 2

print(f"The final number of passengers is : {passengers_counter}")