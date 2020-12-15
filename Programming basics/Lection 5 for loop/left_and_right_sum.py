numbers_to_read = int(input())
left_sum = 0
right_sum = 0
for i in range(0, numbers_to_read):
    left_numbers = int(input())
    left_sum += left_numbers
for i in range(0, numbers_to_read):
    right_numbers = int(input())
    right_sum += right_numbers
if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
elif left_sum != right_sum:
    print(f'No, diff = {abs(left_sum - right_sum)}')
