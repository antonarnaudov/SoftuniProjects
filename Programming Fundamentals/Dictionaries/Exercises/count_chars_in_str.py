def validate_key(dictionary, key, value=0):
    if key not in dictionary:
        my_dict[key] = value


def print_dict(dictionary):
    for k, v in dictionary.items():
        print(f'{k} -> {v}')


a = input()
my_dict = {}

for ch in a:
    if ch == ' ':
        continue
    validate_key(my_dict, ch)
    my_dict[ch] += 1
print_dict(my_dict)
