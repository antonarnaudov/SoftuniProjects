# 1 - push
# 2 - pop
# 3 - print max element
# 4 - print max element
# last - print all elements

n = int(input())
query = []

for _ in range(n):
    num = input().split()

    if num[0] == "1":
        query.append(int(num[1]))

    elif num[0] == "2":
        if query:
            query.pop()
        continue

    elif num[0] == "3":
        if query:  # !!!!!!!!!!!!!!!!!!!!!!!!!
            print(max(query))

    elif num[0] == "4":
        if query:  # !!!!!!!!!!!!!!!!!!!!!!!!!
            print(min(query))

print(', '.join([str(x) for x in reversed(query)]))
