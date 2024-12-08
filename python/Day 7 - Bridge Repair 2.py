import itertools as iter

input = list()

with open("input/day_07.txt", "r") as file:
    for line in file:
        sep = line.rstrip().split(" ")
        sep[0] = sep[0][:-1]
        input.append(sep)

output = 0

for n, items in enumerate(input):
    #print(n)
    target = int(items[0])
    items = items[1:]

    is_eq_target = False

    for operators in iter.product(['*', '+', '||'], repeat = len(items) - 1):
        running = items[1:]
        total = int(items[0])
        for operation, num in zip(operators, running):
            match operation:
                case '+':
                    total = total + int(num)
                case '*':
                    total = total * int(num)
                case '||':
                    total = int(str(total)+str(num))
            
            if total > target:
                break
                    
        if total == target:
            is_eq_target = True
    
    if is_eq_target == True:
        output += target

    #print(target, items)

print(output)