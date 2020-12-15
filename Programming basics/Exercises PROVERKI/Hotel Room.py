season = input()
nights_count = int(input())

if season == "May" or season == "October":
    studio_price = 50 * nights_count
    apartment_price = 65 * nights_count
    if nights_count > 7 and nights_count < 14:
        studio_price = studio_price - studio_price * 0.05
    elif nights_count > 14:
        studio_price = studio_price - studio_price * 0.3
    else:
        studio_price = studio_price
    apartment_price = 65 * nights_count
    if nights_count > 14:
        apartment_price = apartment_price - apartment_price * 0.1
    else:
        apartment_price = 65 * nights_count

elif season == "June" or season == "September":
    studio_price = 75.20 * nights_count
    apartment_price = 68.70 * nights_count
    if nights_count > 14:
        studio_price = studio_price - studio_price * 0.2
        apartment_price = apartment_price - apartment_price * 0.1
    else:
        studio_price = studio_price
        apartment_price = apartment_price

elif season == "July" or season == "August":
    studio_price = 76 * nights_count
    apartment_price = 77 * nights_count
    if nights_count > 14:
        apartment_price = apartment_price - apartment_price * 0.1
    else:
        apartment_price = apartment_price

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
