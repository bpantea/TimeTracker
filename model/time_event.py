from model.event import Event
from model.timestamp import Timestamp


class TimeEvent(object):
    def __init__(self, event: Event, timestamp: Timestamp):
        self.event = event
        self.timestamp = timestamp

    @staticmethod
    def from_str(line: str):
        values = line.split()
        event = Event.from_str(values[0])
        time = Timestamp.from_str(values[1])
        return TimeEvent(event, time)

    def to_str(self):
        return self.event.to_str() + ' ' + self.timestamp.to_str()

    def __str__(self):
        return "TimeEvent: {event: " + str(self.event) + ' ' + str(self.timestamp) + "} "
