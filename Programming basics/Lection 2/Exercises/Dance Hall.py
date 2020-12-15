import math

L = float(input())
W = float(input())
A = float(input())

hallSise = (L * 100) * (W * 100)
wordrobeSise = (A*100)**2
benchSise = hallSise/10
freeSpace =  hallSise - wordrobeSise - benchSise

dancersNum = freeSpace/(40+7000)

print(math.floor(dancersNum))

#komandata math.floor zakruglq do nai blizkoto chislo nadolu