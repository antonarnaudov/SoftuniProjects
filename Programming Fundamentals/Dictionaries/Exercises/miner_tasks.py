def validate_key(dictionary, key, value=0):
    if key not in dictionary:
        resources[key] = value


def print_dict(dictionary):
    for k, v in dictionary.items():
        print(f'{k} -> {v}')


resources = {}

while True:
    resource = input()
    if resource == 'stop':
        break

    quantity = int(input())

    validate_key(resources, resource)
    resources[resource] += quantity

print_dict(resources)
