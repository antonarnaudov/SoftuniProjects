# stack e inbuilt v list

# stack functions
# append
# pop
print('LIST')
l = [1, 2, 3, 4]
print(l)

l.append(5)
print(l)

l.insert(1, -777)
print(l)

l.pop()
print(l)

# list
# dynamic size
#   - grow
#   - shrink
# random element access
#   - first [0]
#   - middle [5]
#   - last [7], [-1]

# --------------------------------------------------------- #
print('----------------------------------------------------')
print('STACK')

# Stack
# dynamic size
#   - grow -> append(el)
#   - shrink -> pop(el)

# element access at the end
#   - current (last element) ([-1])

s = []

s.append(3)
s.append(5)
s.append(7)
print(s)

while s:
    print(s.pop())
