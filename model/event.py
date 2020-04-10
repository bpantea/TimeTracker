from enum import Enum


class Event(Enum):
    START = 1
    END = 2
    SET = 3

    @staticmethod
    def from_str(line: str):
        return Event(int(line))

    def to_str(self):
        return str(self.value)
