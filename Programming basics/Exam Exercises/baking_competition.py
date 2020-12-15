participants_count = int(input())

participants_counter = 0
current_participant_name = ''

cookies = 0
cakes = 0
waffles = 0

all_cookies_sold = 0
all_cakes_sold = 0
all_waffles_sold = 0

all_bakery_sold = 0
total_sum_for_charity = 0

cookies_price = 1.50
cakes_price = 7.80
waffles_price = 2.30

while participants_count > participants_counter:
    Participant_name = input()
    current_participant_name = Participant_name

    while Participant_name == current_participant_name:
        sweet_type = input()
        if sweet_type == 'Stop baking!':
            print(f'{current_participant_name} baked {cookies} cookies, {cakes} cakes and {waffles} waffles.')
            current_participant_name = ''
            participants_counter += 1
            cookies = 0
            cakes = 0
            waffles = 0
            break

        sweets_count = int(input())
        if sweet_type == 'cookies':
            cookies += sweets_count
            all_cookies_sold += sweets_count

        elif sweet_type == 'cakes':
            cakes += sweets_count
            all_cakes_sold += sweets_count

        elif sweet_type == 'waffles':
            waffles += sweets_count
            all_waffles_sold += sweets_count

        all_bakery_sold = all_cookies_sold + all_cakes_sold + all_waffles_sold
        total_sum_for_charity = (all_cookies_sold * cookies_price) + (all_cakes_sold * cakes_price) + (all_waffles_sold * waffles_price)

print(f'All bakery sold: {all_bakery_sold}')
print(f'Total sum for charity: {total_sum_for_charity:.2f} lv.')