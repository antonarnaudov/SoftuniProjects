import sys

count_numbers = int(input())
smallest = sys.maxsize
biggest = -sys.maxsize

for amount in range(count_numbers):
    current_number = int(input())
    if current_number > biggest:
        biggest = current_number
    if current_number < smallest:
        smallest = current_number
print(f'Max number: {biggest}')
print(f'Min number: {smallest}')