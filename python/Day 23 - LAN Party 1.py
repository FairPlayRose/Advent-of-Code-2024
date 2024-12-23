from typing import Self

input: list[str] = list()

with open("input/day_23_test.txt", "r") as file:
    for line in file:
        input.append(line.rstrip())
        
class LANConcention:
    def __init__(self, PC1: str, PC2: str):
        self.PC1 = PC1
        self.PC2 = PC2
        
    def combine_one(self, other: Self) -> str | None:
        match other.PC1, other.PC2:
            case self.PC1, _:
                return self.PC2 + ',' + self.PC1 + ',' + other.PC2
            case self.PC2, _:
                return self.PC1 + ',' + self.PC2 + ',' + other.PC2
            case _, self.PC1:
                return self.PC2 + ',' + self.PC1 + ',' + other.PC1
            case _, self.PC2:
                return self.PC1 + ',' + self.PC2 + ',' + other.PC1
            case _:
                return None
    
    def combine_many(self, others: list[Self]) -> list[str]:
        return [self.combine_one(other) for other in others if self.combine_one(other) != None]

connnection_list = [LANConcention(*line.split('-')) for line in input]

sublist = list()

for i, connenction in enumerate(connnection_list):
    sublist = sublist + connenction.combine_many(connnection_list[i+1:])

#print(connnection_list)
for item in sublist:
    print(item)