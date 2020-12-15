def result(a, b):
    chr_list = []
    for i in range(first + 1, second):
        chr_list.append(chr(i))
    # chr_list.remove(chr(first))
    # chr_list.remove(chr(second))

    print(*chr_list, sep=' ')


a = input()
b = input()

first = ord(a)
second = ord(b)

result(a, b)

# a = input()
# b = input()
#
# chr_list = []
#
# first = ord(a)
# second = ord(b)
#
# for i in range(first, second + 1):
#     chr_list.append(chr(i))
# chr_list.remove(chr(first))
# chr_list.remove(chr(second))
#
# print(*chr_list, sep=' ')
