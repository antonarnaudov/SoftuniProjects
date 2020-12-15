class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        # if self.hours < 10:
        #     self.hours = '0' + str(self.hours)
        #
        # if int(self.minutes) < 10:
        #     self.minutes = '0' + str(self.minutes)
        #
        # if int(self.seconds) < 10:
        #     self.seconds = '0' + str(self.seconds)

        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self):
        if self.seconds + 1 > Time.max_seconds:
            self.seconds = 0
            if self.minutes + 1 > Time.max_minutes:
                self.minutes = 0
                if self.hours + 1 > Time.max_hours:
                    self.hours = 0
                else:
                    self.hours = self.hours + 1
            else:
                self.minutes = self.minutes + 1
        else:
            self.seconds = self.seconds + 1

        return Time.get_time(self)


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
t = Time(1, 20, 30)
print(t.get_time())

