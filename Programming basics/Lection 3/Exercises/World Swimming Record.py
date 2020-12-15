#from math import floor
#record_seconds = float(input())
#area_meter = float(input())
#time_seconds = float(input())

#swim = area_meter * time_seconds
#resistance = area_meter//15
#resistance = resistance * 12.5
#resistance = floor(resistance)

#time_sum = swim + resistance

#if record_seconds > time_sum:
    #diff = abs(time_sum - record_seconds)
    #print(f"Yes, he succeeded! The new world record is {diff:.2f} seconds.")
#elif record_seconds < time_sum:
    #print(f"No, he failed! He was {time_sum:.2f} seconds slower.")

record_in_seconds = float(input())
distance_in_meters = float(input())
time_per_meter_seconds = float(input())

record_to_beat = distance_in_meters * time_per_meter_seconds
slow_down = (distance_in_meters // 15) * 12.5

total_time = record_to_beat + slow_down

if record_in_seconds > total_time:
    print(f"Yes, he succeeded! The new world record is {abs(total_time):.2f} seconds.")
else:
    time = record_in_seconds - total_time
    print(f"No, he failed! He was {abs(time):.2f} seconds slower.")