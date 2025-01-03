from functools import cache

input: list[str] = list()

with open("input/day_19.txt", "r") as file:
    for line in file:
        input.append(line.rstrip())

towels = [x.strip() for x in input[0].split(",")]
towels.sort()

longest_pattern = max([len(towel) for towel in towels])
#print(longest_pattern)

designs = input[2:]

@cache
def recursive_design_check(design: str) -> bool:
    # If the design is empty we have constructed it from towels
    if not design:
        return True
    
    check_list = [recursive_design_check(design[i:])
                  for i in reversed(range(1,longest_pattern))
                  if design[:i] in towels]
    #print(check_list)
    
    return any(check_list)

#test = recursive_design_check(designs[0])
#print(test)

checksum = 0

for design in designs:
    checksum += int(recursive_design_check(design))

print(checksum)