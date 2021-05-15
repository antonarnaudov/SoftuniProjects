n = int(input())

for x in range(n, 0, -1):
    ll = [' ' * (n - x)]
    for y in range(1, x + 1):
        ll.append(y)
    ll2 = ll.copy()
    ll2.pop()
    ll2.reverse()
    ll += ll2
    print(''.join([str(x) for x in ll]))
    ll.clear()
    ll2.clear()
