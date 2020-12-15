string = str(input())
repeat = int(input())


def repeat_string(word, repeater):
    result = ''
    for _ in range(0, repeater):
        result += string
    return result


print(repeat_string(string, repeat))
