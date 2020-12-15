def result_expression(text):
    s = []
    result = []

    for index in range(len(text)):
        ch = text[index]

        if ch == '(':
            s.append(index)

        elif ch == ')':
            start_index = s.pop()
            result.append(text[start_index:index + 1])

    return result


i = str(input())
for subexpression in result_expression(i):
    print(subexpression)
