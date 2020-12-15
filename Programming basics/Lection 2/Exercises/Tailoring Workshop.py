countTables = int(input())
lenghtTables = float(input())
widthTables = float(input())

visi = 0.30

ploshtPokrivki = countTables * (lenghtTables + 2 * visi) * (widthTables + 2 * visi)
ploshtKareta = countTables * (lenghtTables/2) * (lenghtTables/2)

USD = ploshtKareta * 9 + ploshtPokrivki * 7
LEV = USD * 1.85

print(f'{USD:.2f} USD')
print(f'{LEV:.2f} BGN')


#Цена в долари: 8.80 * 7 долара + 1.25 * 9 долара = 72.85 долара
#Цена в левове: 72.85 * 1.85 = 134.77 лева


#count_Tabes = int(input())
#lenght_Tables = float(input())
#width_Tables = float(input())

#area_Pokrivka = count_Tabes *(lenght_Tables+2*0.3)*(width_Tables+2*0.3)
#area = count_Tabes *(lenght_Tables/2)*(lenght_Tables/2)
#priceUSD = area_Pokrivka * 7 + area * 9
#priceBGN = priceUSD*1.85

#print(f'{priceUSD:.2f} USD')
#print(f'{priceBGN:.2f} BGN')
