import re

input = list()

with open("input/day_03.txt", "r") as file:
    for line in file:
        result = re.findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don't\(\))", line)
        result = [a+b+c for a,b,c in result]

        do_stuff = True
        for group in result:
            if group == 'do()':
                do_stuff = True
            elif group == "don't()":
                do_stuff = False
            elif do_stuff == True:
                numbers = re.findall(r"([0-9]{1,3})", group)
                input.append(int(numbers[0]) * int(numbers[1]))

    
print(sum(input))


