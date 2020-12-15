# count again

asd = [1, 2, 3]

end = 10
counter = 0
i = len(asd) - 1

while counter < end:
    if i == -1:
        i = len(asd) - 1

    print(asd[i])
    i -= 1
    counter += 1
