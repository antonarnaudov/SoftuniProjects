numbers = [int(x) for x in reversed(input().split())]
rack_capacity = int(input())
pack = 0
racks = 0

for n in numbers:
    pack += n
    if pack >= rack_capacity:
        racks += 1
        pack -= rack_capacity
        if pack:
            racks += 1
            pack = 0

# if pack:
#     racks += 1
print(racks)
