#ozeleneni = float(input())
#priceOzelenqvane = ozeleneni * 7.61
#discount = 0.18 * priceOzelenqvane
#finalPrice = priceOzelenqvane - discount
#print(f'The final price is: {finalPrice:.2f} lv.')
#print(f'The discount is: {discount:.2f} lv.')


ozeleneni = float(input())

Cena1Kvm = 7.61
otstupka = 0.18

cenaOzelenqvane = ozeleneni * Cena1Kvm
prispadaneOtstupka = otstupka * cenaOzelenqvane
krainaCena = cenaOzelenqvane - prispadaneOtstupka

print(f'The final price is: {krainaCena:.2f} lv.')
print(f'The discount is: {prispadaneOtstupka:.2f} lv.')