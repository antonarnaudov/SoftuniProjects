def result(x1, y1, x2, y2):
    num_list = [x1, y1, x2, y2]
    for _ in range(2):
        num_list.remove(max(num_list))
    f = num_list[0]
    g = num_list[1]

    print(f"({f}, {g})")
    print(f"({', '.join(num_list)})")


a = int(input())
b = int(input())
c = int(input())
d = int(input())
result(a, b, c, d)
