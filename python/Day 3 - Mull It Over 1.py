import re

input = list()

with open("input/day_03.txt", "r") as file:
    for line in file:
        result = re.findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\))", line)
        for mult in result:
            numbers = re.findall(r"([0-9]{1,3})", mult)
            input.append(int(numbers[0]) * int(numbers[1]))

print(sum(input))
