reservation_day = int(input())
reservation_month = int(input())

accommodation_day = int(input())
accommodation_month = int(input())

leaving_day = int(input())
leaving_month = int(input())

discount = 0
price_per_night = 0
discount_days = accommodation_day - 10
days_staying = abs(accommodation_day - leaving_day)

if reservation_day <= 1:
    pass