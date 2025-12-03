from dataclasses import dataclass


@dataclass
class Range():
    start_num: int
    end_num: int

    @staticmethod
    def create(start: str, end: str):
        return Range(int(start), int(end))
