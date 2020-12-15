budget = float(input())

budget_counter = budget
items_count = 0
money_spent = 0
finish = False
while budget > 0:
    star_price = 5.69
    angel_price = 8.49
    lights_price = 11.20
    wreath_price = 15.50
    candle_price = 3.59

    product_type = input()

    if product_type == 'Finish':
        print("Congratulations! You bought everything!")
        finish = True
        break

    items_count += 1

    if product_type == 'Star':
        if items_count % 3 == 0:
            star_price_discount = star_price * 0.3
            star_price = star_price - star_price_discount
        budget -= star_price
        if budget < 0:
            items_count -= 1
            budget = abs(budget)
            break
        money_spent += star_price

    elif product_type == 'Angel':
        if items_count % 3 == 0:
            angel_price_discout = angel_price * 0.3
            angel_price = angel_price - angel_price_discout
        budget -= angel_price
        if budget < 0:
            items_count -= 1
            budget = abs(budget)
            break
        money_spent += angel_price

    elif product_type == 'Lights':
        if items_count % 3 == 0:
            lights_price_discount = lights_price * 0.3
            lights_price = lights_price - lights_price_discount
        budget -= lights_price
        if budget < 0:
            items_count -= 1
            budget = abs(budget)
            break
        money_spent += lights_price

    elif product_type == 'Wreath':
        if items_count % 3 == 0:
            wreath_price_discount = wreath_price * 0.3
            wreath_price = wreath_price - wreath_price_discount
        budget -= wreath_price
        if budget < 0:
            items_count -= 1
            budget = abs(budget)
            break
        money_spent += wreath_price

    elif product_type == 'Candle':
        if items_count % 3 == 0:
            candle_price_discount = candle_price * 0.3
            candle_price = candle_price - candle_price_discount
        budget -= candle_price
        if budget < 0:
            items_count -= 1
            budget = abs(budget)
            break
        money_spent += candle_price

# money_needed = money_spent - budget_counter
if not finish:
    print(f"Not enough money! You need {budget:.2f}lv more.")

print(f"{items_count} items -> {money_spent:.2f}lv spent.")