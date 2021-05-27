class Clock:
    def __init__(self, hour, minute):
        self.hour = (hour + minute // 60) % 24
        self.minute = minute % 60

    def __repr__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        minutes += self.minute
        hours = self.hour
        hours += minutes // 60
        minutes %= 60
        hours %= 24

        return Clock(hours, minutes)

    def __sub__(self, minutes):
        minutes = self.minute - minutes
        hours = self.hour
        hours += minutes // 60
        minutes %= 60
        hours %= 24

        return Clock(hours, minutes)
