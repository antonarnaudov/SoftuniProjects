holiday_days = int(input())

daily_limit = 60
expenses_counter = 0
money_left = 0
products_count = 0
days_counter = 0
# for days in range(holiday_days + 1):
skip = False
too_big = False
exceeded = False
while holiday_days > days_counter:
    command_or_price = input()
    exceeded = False
    skip = False
    too_big = False
    if command_or_price == 'Day over':
        if expenses_counter < daily_limit:
            money_left = daily_limit - expenses_counter
            daily_limit = 60 + money_left
            days_counter += 1
        print(f"Money left from today: {money_left:.2f}. You've bought {products_count} products.")
        expenses_counter = 0
        products_count = 0
        skip = True

    if not skip:
        command_or_price = int(command_or_price)
        if command_or_price > daily_limit:
            expenses_counter = 0
            too_big = True
        if not too_big:
            expenses_counter += command_or_price
            products_count += 1

        if expenses_counter >= daily_limit:
            days_counter += 1
            print(f"Daily limit exceeded! You've bought {products_count} products.")
            daily_limit = 60
            products_count = 0
            expenses_counter = 0
            exceeded = True
        if not exceeded:
            daily_limit = daily_limit - expenses_counter
            expenses_counter = 0
    print(f'Daily limit is: {daily_limit}')