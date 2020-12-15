numbers = input().split()
remove = int(input())
num_list = []

for n in numbers:
    num_list.append(int(n))

for _ in range(remove):
    num_list.remove(min(num_list))

print(num_list)

# list = [90, 100, 95, 95]
# list.remove(min(list))
# print(list)

# num_list = []
# for _ in range(3):
#     a = int(input())
#     num_list.append(a)
# for _ in range(2):
#     num_list.remove(max(num_list))
# print(*num_list, sep='')
