start = int(input())
end = int(input())
magick_num = int(input())
combinations = 0
is_found = False

for x1 in range(start, end + 1):
    for x2 in range(start, end +1):
        combinations += 1
        if x1 + x2 == magick_num:
            print(f"Combination N:{combinations} ({x1} + {x2} = {magick_num})")
            is_found = True
            break
    if is_found:
        break
if not is_found:
    print(f'{combinations} combinations - neither equals {magick_num}')