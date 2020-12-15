files = list(zip(input().split(', '), input().split(', ')))
[print(f'{x[0]} -> {x[1]}') for x in files]
