input = list()

is_safe_positive = lambda n: 4 > n > 0
is_safe_negative = lambda n: 0 > n > -4

with open("input/day_02.txt", "r") as file:
    for line in file:
        report = line.rstrip().split(" ")
        lenght = len(report)
        differens = [int(report[i]) - int(report[i+1]) for i in range(lenght-1)]
        is_all_safe_positive = all(list(map(is_safe_positive, differens)))
        is_all_safe_negative = all(list(map(is_safe_negative, differens)))
        input.append((is_all_safe_positive or is_all_safe_negative))

print(sum(input))