from math import ceil

nums = list(map(int, input().split(', ')))

max_num = max(nums)

groups_count = ceil(max_num / 10)

# for group in range(1, groups_count + 1):
#     group_nums = []
#
#     minimum = group * 10 - 10
#     maximum = group * 10
#
#     for num in nums:
#         if minimum < num <= maximum:
#             group_nums.append(num)
#
#     print(f"Group of {group * 10}'s: {group_nums}")

for group in range(1, groups_count + 1):

    minimum = group * 10 - 10
    maximum = group * 10
    group_nums = []

    groups_count = [num for num in nums if minimum < num < maximum]
    print(f"Group of {group * 10}'s: {group_nums}")