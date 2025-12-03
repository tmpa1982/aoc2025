from dataclasses import dataclass


@dataclass
class Range():
    start_str: str
    end_str: str
    start_num: int
    end_num: int

    @staticmethod
    def create(start: str, end: str):
        return Range(start, end, int(start), int(end))
