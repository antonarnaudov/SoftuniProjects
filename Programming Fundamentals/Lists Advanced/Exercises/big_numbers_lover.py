# 1
# def parse_str_to_int(string):
#     return int(string)

# 1
# list_int = list(map(parse_str_to_int, list_str))

# 2
# list_str = sorted(list_str, reverse=True)

# 3
# list_str.sort(reverse=True)

# 4
# list_int = list(map(lambda string: int(string), list_str))

list_str = input().split(' ')

list_str = sorted(list_str, reverse=True)

list_int = list(map(int, list_str))

print(''.join(map(str, list_int)))
# print(''.join(list_str))
