from collections import Counter

input = list()

is_safe_positive = lambda n: 4 > n > 0
is_safe_negative = lambda n: 0 > n > -4

is_safe_range = lambda n: 4 > abs(n) > 0
is_pos = lambda n: n > 0
is_neg = lambda n: n < 0

with open("input/day_02.txt", "r") as file:
    for line in file:
        report = line.rstrip().split(" ")
        lenght = len(report)
        
        output = []
        for n in range(lenght):
            report_pop_one = report.copy()
            report_pop_one.pop(n)
            differens = [int(report_pop_one[i]) - int(report_pop_one[i+1]) for i in range(lenght-2)]
            is_all_safe_positive = all(list(map(is_safe_positive, differens)))
            is_all_safe_negative = all(list(map(is_safe_negative, differens)))
            output.append((is_all_safe_positive or is_all_safe_negative))
        
        input.append(any(output))

print(sum(input))
