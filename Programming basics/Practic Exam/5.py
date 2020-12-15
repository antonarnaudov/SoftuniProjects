days_count = int(input())
food_quantity = float(input())

food_eaten_sum = 0
dog_food_counter = 0
cat_food_counter = 0
biscuits_counter = 0
days_counter = 0

while days_count > days_counter:
    food_eaten_dog = int(input())
    food_eaten_cat = int(input())
    days_counter += 1
    if days_counter % 3 == 0:
        biscuit = (food_eaten_dog + food_eaten_cat) * 0.1
        biscuits_counter += biscuit
    dog_food_counter += food_eaten_dog
    cat_food_counter += food_eaten_cat

food_eaten_sum = dog_food_counter + cat_food_counter

food_eaten_percent = food_eaten_sum / food_quantity
food_eaten_percent *= 100

dog_food_percent = dog_food_counter / food_eaten_sum
dog_food_percent *= 100

cat_food_percent = cat_food_counter / food_eaten_sum
cat_food_percent *= 100

print(f"Total eaten biscuits: {biscuits_counter:.0f}gr.")
print(f"{food_eaten_percent:.2f}% of the food has been eaten.")
print(f"{dog_food_percent:.2f}% eaten from the dog.")
print(f"{cat_food_percent:.2f}% eaten from the cat.")