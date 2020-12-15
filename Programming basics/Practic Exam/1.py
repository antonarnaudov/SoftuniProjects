from math import ceil
area_length = float(input())
area_width = float(input())
bar_area = float(input())

area = area_length * area_width
bar = bar_area * bar_area
dancingh_area = area * 0.19
free_space = area - bar - dancingh_area
people = ceil(free_space / 3.2)
print(people)
