daysActive = int(input())
countSweets = int(input())
countCakes = int(input())
countWaffles = int(input())
countPancakes = int(input())

cakePerDay = countCakes * 45
wafflePerDay = countWaffles * 5.80
pancakePerDay = countPancakes * 3.20
sumPerDay = (cakePerDay + wafflePerDay + pancakePerDay) * countSweets

allSum = sumPerDay * daysActive

productsUsedSum = allSum - (0.125 * allSum)

print(f'{productsUsedSum:.2f}')