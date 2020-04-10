from datetime import datetime

from model.Event import Event
from model.TimeEvent import TimeEvent
from model.Timestamp import Timestamp
from repository import TimeEventRepository


class TimeService:
    def __init__(self, repo: TimeEventRepository):
        self.repo = repo

    def start_time(self, hours: int = None, minutes: int = None):
        self.__add_event(Event.START, hours, minutes)

    def end_time(self, hours: int = None, minutes: int = None):
        self.__add_event(Event.END, hours, minutes)

    def set_time(self, hours: int = None, minutes: int = None):
        self.__add_event(Event.SET, hours, minutes)

    def __add_event(self, event: Event, hours: int = None, minutes: int = None):
        if hours is None or minutes is None:
            timestamp = Timestamp(TimeService.__current_time_in_minutes())
        else:
            timestamp = Timestamp(hours * 60 + minutes)
        self.repo.add_time_event(TimeEvent(event, timestamp))

    def __calculate_time(self):
        time = 0
        last_start = None
        events = self.repo.get_all()
        for el in events:
            if el.event is Event.START:
                last_start = el.timestamp
            elif el.event is Event.END:
                if last_start is not None:
                    time += el.timestamp - last_start
                    last_start = None
            elif el.event is Event.SET:
                time = el.timestamp.minutes
                last_start = None
        if len(events) > 0 and events[-1].event is Event.START:
            time += TimeService.__current_time_in_minutes() - events[-1].timestamp.minutes
        return time, last_start

    @staticmethod
    def __current_time_in_minutes():
        hours = datetime.today().hour
        minutes = datetime.today().minute
        return hours * 60 + minutes

    def formatted_time(self):
        minutes, last_start = self.__calculate_time()
        response = "Current tracked time: " + str(minutes // 60) + " hours and " + str(minutes % 60) + " minutes."
        if last_start is not None:
            response += '\nLast time you started tracking: ' + str(last_start)
        return response
