exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

#convert exam hours and minutes -> minutes

exam_time_in_min = exam_hour* 60 + exam_min
arrival_time_in_min = arrival_hour * 60 + arrival_min
diff = exam_time_in_min - arrival_time_in_min

if diff < 0:
    print('Late')
    diff = abs(diff)
    if diff >= 60:
        hours = diff // 60
        minutes = diff % 60
        print(f'{hours}:{minutes:02d} hours after the start')
    else:
        print(f'{diff} minutes after the start')
elif 0 <= diff <= 30:
    print('On time')
    if diff > 0:
        print(f'{diff} minutes before the start')
#early
elif diff > 30:
    print('Early')
    if diff >= 60:
        hours = diff // 60
        minutes = diff % 60
        print(f'{hours}:{minutes:02d} hours before the start')
    else:
        print(f'{diff} minutes before the start ')
