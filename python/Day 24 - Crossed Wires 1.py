import re

input_start: dict[str, bool] = dict()
input_gates: list[str] = list()
outputs: list[str]

with open("input/day_24.txt", "r") as file:
    #print(file.read().split('\n\n'))
    #string = file.read().split('\n\n')
    #start = string[0]
    #gates = string[1]
    start, gates = file.read().split('\n\n')
    outputs = re.findall('z[0-9]{2}', gates)
    for line in start.split('\n'):
        name, bit = line.split(': ')
        input_start[name] = bool(int(bit))
    for line in gates.split('\n'):
        input_gates.append(line.rstrip())

#print(input_start)
#print(input_gates)

def operanding(left: bool, operand: str, right: bool) -> bool:
    match operand:
        case 'XOR':
            return left ^ right
        case 'OR':
            return left or right
        case 'AND':
            return left and right

while input_gates:
    current_gate = input_gates.pop(0)
    left, operand, right, _, out = current_gate.split()
    if left in input_start and right in input_start:
        input_start[out] = operanding(input_start[left], operand, input_start[right])
    else:
        input_gates.append(current_gate)

#print(input_start)

#print(list(reversed(sorted(outputs))))

output = ''.join([str(int(input_start.get(outputgate, False))) for outputgate in reversed(sorted(outputs))])
#print(output)
output = int(output, 2)

print(output)

