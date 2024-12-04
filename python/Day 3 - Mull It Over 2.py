import re

input = list()

with open("input/day_03_test_2.txt", "r") as file:
    for line in file:
        result = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do\(\))|(don't\(\))", line)
        print(result)

        do_stuff = True
        for group in result:
            match group:
                case (a, b, '', '') if do_stuff == True:
                    input.append(int(a)*int(b))
                case ('', '', 'do()', ''):
                    do_stuff = True
                case ('', '', '', "don't()"):
                    do_stuff = False
    
print(sum(input))


