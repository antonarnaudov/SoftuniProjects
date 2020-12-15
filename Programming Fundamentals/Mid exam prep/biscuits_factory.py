from math import floor
biscuits_per_day = int(input())  # per worker
workers_count = int(input())
second_factory = int(input())

biscuits_per_month = 0
for day in range(1, 30 + 1):
    if day % 3 == 0:
        percent = floor((biscuits_per_day * workers_count) * 0.75)
        biscuits_per_month += percent
    else:
        biscuits_per_month += biscuits_per_day * workers_count

print(f"You have produced {biscuits_per_month} biscuits for the past month.")

difference = abs(biscuits_per_month - second_factory)
percent = (difference / second_factory) * 100

if biscuits_per_month > second_factory:
    print(f"You produce {percent:.2f} percent more biscuits.")
else:
    print(f"You produce {percent:.2f} percent less biscuits.")
