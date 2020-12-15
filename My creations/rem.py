from math import ceil

info_input = input().split(' ')

length = int(info_input[0])
width = int(info_input[1])
height = int(info_input[2])

one_bucket = 16

area = (length * height) * 2 + (width * height) * 2

result = ceil(area / one_bucket)

print(result)
