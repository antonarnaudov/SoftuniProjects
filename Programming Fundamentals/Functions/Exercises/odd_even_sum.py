def odd_even_sum(text):
    even = 0
    odd = 0
    for i in text:
        index = int(i)
        if index % 2 == 0:
            even += index
        else:
            odd += index
    return f'Odd sum = {odd}, Even sum = {even}'


text = input()
print(odd_even_sum(text))
