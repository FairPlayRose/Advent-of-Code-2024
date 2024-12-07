import itertools as iter

input = list()

with open("input/day_07.txt", "r") as file:
    for line in file:
        sep = line.rstrip().split(" ")
        sep[0] = sep[0][:-1]
        input.append(sep)

output = 0

for items in input:
    target = items[0]
    items = items[1:]

    is_eq_target = False

    for operators in iter.product(['+', '*'], repeat = len(items) - 1):
        running = items[::-1]
        for operation in operators:
            x = int(running.pop())
            y = int(running.pop())
            match operation:
                case '+':
                    running.append(x + y)
                case '*':
                    running.append(x * y)
        if running[0] == int(target):
            is_eq_target = True
    
    if is_eq_target == True:
        output += int(target)

    #print(target, items)

print(output)