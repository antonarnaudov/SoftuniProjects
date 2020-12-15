wiskyCostLV = float(input())
beerLiter = float(input())
wineLiter = float(input())
rakiqLiter = float(input())
wiskyLiter = float(input())

rakiqPricePerLiter = wiskyCostLV / 2
winePricePerLiter = rakiqPricePerLiter - (rakiqPricePerLiter * 0.4)
beerPricePerLiter = rakiqPricePerLiter - (rakiqPricePerLiter * 0.8)

sumRakiq = rakiqLiter * rakiqPricePerLiter
sumWine = wineLiter * winePricePerLiter
sumBeer = beerLiter * beerPricePerLiter
sumWisky = wiskyLiter * wiskyCostLV
allSum = sumRakiq + sumWine + sumBeer + sumWisky

print(f'{allSum:.2f} Lv')