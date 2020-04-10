from datetime import time


class Timestamp(object):
    def __init__(self, minutes: int):
        self.minutes = minutes

    def __str__(self):
        return time(minute=self.minutes % 60, hour=self.minutes // 60).strftime("%H:%M")

    @staticmethod
    def from_str(line: str):
        return Timestamp(int(line))

    def to_str(self):
        return str(self.minutes)

    def __sub__(self, other):
        if not isinstance(other, Timestamp):
            return 0
        return self.minutes - other.minutes
