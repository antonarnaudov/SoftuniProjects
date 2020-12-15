lenghtCM = int(input())
widthCM = int(input())
heightCM = int(input())
areaProcent = float(input())  #float - drobno chislo // int - cqlo

area = lenghtCM * widthCM * heightCM
availableLiters = area * 0.001
percent = areaProcent * 0.01
literNeeded = availableLiters*(1-percent)
print(f'{literNeeded:.3f}')



L = int(input())
W = int(input())
H = int(input())
areaPercent = float(input())

area = L * W * H
literSum = area * 0.001
percent = areaPercent * 0.01
AllLitersNeeded = literSum * (1 - percent)

print(f'{AllLitersNeeded:.3f}')