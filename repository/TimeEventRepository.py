from model.TimeEvent import TimeEvent
from os import path


class TimeEventRepository(object):
    def __init__(self, filename: str = None):
        self.list = []
        self.filename = filename
        self.load()

    def load(self):
        if not path.exists(self.filename):
            return
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                self.list.append(TimeEvent.from_str(line))

    def __write_time_event(self, value: TimeEvent):
        with open(self.filename, self.__get_output_mode()) as f:
            f.write(value.to_str() + '\n')

    def add_time_event(self, time_event: TimeEvent):
        self.list.append(time_event)
        self.__write_time_event(time_event)

    def get_all(self):
        return self.list

    def __get_output_mode(self):
        if not path.exists(self.filename):
            return 'w'
        else:
            return 'a'
