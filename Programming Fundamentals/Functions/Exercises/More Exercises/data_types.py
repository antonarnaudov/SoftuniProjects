def result(command, info):
    if command == 'int':
        res = int(info) * 2
        print(res)
    elif command == 'real':
        res = float(info) * 1.5
        print(f'{res:.2f}')
    elif command == 'string':
        print(f'${info}$')


command_input = input()
info_input = input()
result(command_input, info_input)
