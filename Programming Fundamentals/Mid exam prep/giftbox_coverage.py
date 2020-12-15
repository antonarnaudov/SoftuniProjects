side_size = float(input())
sheets_number = int(input())
single_sheet_area = float(input())
# percentage can be over 100%
# all numbers are centimeters
sides = 6

area = round(side_size * side_size * sides)

half_covered = 0
for i in range(1, sheets_number + 1):
    if i % 3 == 0:
        half_covered += 1

covered = (sheets_number - half_covered) * single_sheet_area

half_covered = half_covered * single_sheet_area * 0.25
covered_sum = round(covered + half_covered)
percentage = abs(area - covered_sum)

print(f"You can cover {percentage:.2f}% of the box.")
