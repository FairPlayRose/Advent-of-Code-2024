import re

input = list()

with open("input/day_03_test.txt", "r") as file:
    for line in file:
        result = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", line)
        for a,b in result:
            input.append(int(a) * int(b))

print(sum(input))
