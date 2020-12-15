# 1. Read input data
hour = int(input())
minutes = int(input())
# 2. Add 15 to minutes
minutes = minutes + 15
# 3. Check if minutes > 60
# 3.1 Add +1 hour
# 3.2 Calculate minutes left
if minutes >= 60:
    hour = hour + 1
    minutes = minutes - 60
# 4. If hour >= 24 -> hour = 0
if hour >= 24:
    hour = 0
# 5. print
# 5.1 if minutes < 10
if minutes < 10:
    print(f'{hour}:0{minutes}')
# 5.2 if minutes > 10
else:
    print(f'{hour}:{minutes}')