last_sector = str(input())
rows_count_first_sector = int(input())
seats_count_odd_row = int(input())

count_seats = 0

last_sector = ord(last_sector)

for symbols in range(65, last_sector + 1):

    if symbols > 65:
        for rows in range(1, rows_count_first_sector + 1 + 1):

            if rows % 2 == 0:
                # for seats_num in range(1, seats_count_odd_row + 1):
                for seats in range(97, 97 + seats_count_odd_row + 1 + 1):
                    count_seats += 1
                    print(f'{chr(symbols)}{rows}{chr(seats)}')

            elif rows % 2 != 0:
                # for seats_num in range(1, seats_count_odd_row + 1):
                for seats in range(97, 97 + seats_count_odd_row):
                    count_seats += 1
                    print(f'{chr(symbols)}{rows}{chr(seats)}')

    elif symbols == 65:
        for rows in range(1, rows_count_first_sector + 1):
            if rows % 2 == 0:
                # for seats_num in range(1, seats_count_odd_row + 1):
                for seats in range(97, 97 + seats_count_odd_row + 1 + 1):
                    count_seats += 1
                    print(f'{chr(symbols)}{rows}{chr(seats)}')

            elif rows % 2 != 0:
                # for seats_num in range(1, seats_count_odd_row + 1):
                for seats in range(97, 97 + seats_count_odd_row):
                    count_seats += 1
                    print(f'{chr(symbols)}{rows}{chr(seats)}')

print(count_seats)