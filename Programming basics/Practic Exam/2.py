guests_count = int(input())
budget = int(input())

covert_price = guests_count * 20
if covert_price < budget:
    money_left = budget - covert_price
    fireworks_money = money_left * 0.4
    donation_money = money_left - fireworks_money
    print(f"Yes! {fireworks_money:.0f} lv are for fireworks and {donation_money:.0f} lv are for donation.")
else:
    money_needed = covert_price - budget
    print(f"They won't have enough money to pay the covert. They will need {money_needed:.0f} lv more.")