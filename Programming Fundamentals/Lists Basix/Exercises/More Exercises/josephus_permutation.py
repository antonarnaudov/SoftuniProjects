numbers = input().split(' ')
permutation = int(input())

counter = 0
pass_one = True
pass_two = True
result = []
num_list = []

for e in numbers:
    num_list.append(int(e))

while sum(num_list) != 0:

    for i in num_list:

        counter += 1

        if len(num_list) == 3 and counter % permutation == 0 and pass_one == True:
            counter = 2
            pass_one = False
        elif len(num_list) == 2 and counter % permutation == 0 and pass_two == True:
            counter = 5
            pass_two = False

        if counter % permutation == 0:
            result.append(int(i))
            num_list.remove(int(i))
            counter += 1
print(result)
