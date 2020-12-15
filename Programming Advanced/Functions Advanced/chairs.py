def chair_combinations(names, chairs, result=[]):
    if len(result) == chairs:
        print(', '.join(result))
        return

    for i in range(len(names)):
        name = names[i]
        result.append(name)
        chair_combinations(names[i + 1:], chairs, result)
        result.pop()


chair_combinations(input().split(', '), int(input()))
