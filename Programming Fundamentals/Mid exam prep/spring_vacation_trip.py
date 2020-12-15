trip_days = int(input())
budget = float(input())
people_count = int(input())
fuel_per_kilometer = float(input())  # price
food_per_person = float(input())  # price per day
room_per_person = float(input())  # price per day

food_sum = food_per_person * people_count * trip_days
room_sum = room_per_person * people_count * trip_days
if people_count > 10:
    room_sum = room_sum * 0.25
expenses_one = food_sum + room_sum

fuel_sum = 0
for i in range(trip_days):
    kilometers = float(input())
    fuel_sum += kilometers * fuel_per_kilometer
expenses = fuel_sum + expenses_one

more_expenses = 0
for i in range(1, trip_days + 1):
    if i % 3 == 0 or i % 5 == 0:
        more_expenses += expenses * 0.4

expenses = expenses + more_expenses
discount = 0
for i in range(1, trip_days + 1):
    if i % 7 == 0:
        discount += expenses / people_count

expenses = expenses - discount

if budget - expenses > 0:
    result = budget - expenses

    print(f"You have reached the destination. You have {result:.2f}$ budget left.")
else:
    result = expenses - budget
    print(f"Not enough money to continue the trip. You need {result:.2f}$ more.")
