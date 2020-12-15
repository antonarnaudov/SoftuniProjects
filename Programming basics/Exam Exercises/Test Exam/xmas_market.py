from math import floor
money_needed = float(input())
fantasy_count = int(input())
horror_count = int(input())
romantic_count = int(input())

fantasy_price = 14.90
horror_price = 9.80
romantic_price = 4.30

sell_sum = (fantasy_count * fantasy_price) + (horror_count * horror_price) + (romantic_count * romantic_price)
dds = sell_sum * 0.2
sum_after_dds = sell_sum - dds

if sum_after_dds > money_needed:
    workers_receive = sum_after_dds - money_needed
    sellers_receive = floor((sum_after_dds - money_needed) * 0.1)
    giving = (workers_receive - sellers_receive) + money_needed
    print(f'{giving:.2f} leva donated.')
    print(f'Sellers will receive {sellers_receive} leva.')
else:
    print(f'{money_needed - sum_after_dds:.2f} money needed.')