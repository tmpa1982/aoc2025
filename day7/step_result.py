from dataclasses import dataclass


@dataclass
class StepResult:
    row: str
    num_split: int
    
    def __init__(self, row: str, num_split: int):
        self.row = row
        self.num_split = num_split
