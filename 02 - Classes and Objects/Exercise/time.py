class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def get_time(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self):
        self.seconds += 1
        if self.seconds > self.max_seconds:
            self.seconds = 0
            if self.minutes + 1 > self.max_minutes:
                self.hours += 1
                self.minutes = 0
            else:
                self.minutes += 1
            if self.hours > self.max_hours:
                self.hours = 0

        return Time.get_time(self)


time = Time(23, 59, 59)

print(time.next_second())
