
def combo(operand: str):
    trans = {'4': 'A', '5': 'B', '6':'C'}
    return trans.get(operand, operand)

def xor(op1: int, op2: int):
    return op1 ^ op2

def adv(operand: str, register: dict):
    numerator = register['A']
    denominator = 2 ** register[combo(operand)]
    
    register['A'] = numerator // denominator
    
    return register

def bxl(operand: str, register: dict):
    register['B'] = xor(int(operand), register['B'])
    
    return register

def bst(operand: str, register: dict):
    register['B'] = register[combo(operand)] % 8
    
    return register

def jnz(operand: str, pointer: int, register: dict):
    return pointer+2 if register['A'] == 0 else int(operand)

def bxc(operand: str, register: dict):
    register['B'] = xor(register['B'], register['C'])
    return register

def out(operand: str, register: dict, output_: list):
    output_.append(register[combo(operand)] % 8)
    return output_

def bdv(operand: str, register: dict):
    numerator = register['A']
    denominator = 2 ** register[combo(operand)]
    
    register['B'] = numerator // denominator
    
    return register

def cdv(operand: str, register: dict):
    numerator = register['A']
    denominator = 2 ** register[combo(operand)]
    
    register['C'] = numerator // denominator
    
    return register

input = list()

with open("input/day_17_test.txt", "r") as file:
    for line in file:
        input.append(line.rstrip())

def executer(machine: list[str]):
    #print(machine)
    registers = [int(res.split(' ')[-1]) for res in machine[:3]]
    registers = {'0': 0, '1': 1, '2': 2, '3': 3, 'A': registers[0], 'B': registers[1], 'C': registers[2]}
    program: list[str] = machine[-1].split(' ')[-1].split(',')

    output = list()
    pointer = 0

    #print(registers)
    #print(program)

    while pointer < len(program)-1:
        opcode, operand = program[pointer:pointer+2]
        
        print(opcode, pointer)
        
        instruction = {'0': adv,
                    '1': bxl,
                    '2': bst,
                    '3': jnz,
                    '4': bxc,
                    '5': out,
                    '6': bdv,
                    '7': cdv}
        
        if instruction[opcode] == jnz:
            pointer = jnz(operand, pointer, registers)
        elif instruction[opcode] == out:
            output = out(operand, registers, output)
            pointer += 2
        else:
            registers = instruction[opcode](operand, registers)
            pointer += 2
            
        print(output)
            
        print({k: registers[k] for k in ('A', 'B', 'C')})
        #print(program)
    
    #print(''.join([str(x) for x in output]))
    
    registers = {k: registers[k] for k in ('A', 'B', 'C')}
    return registers, output

test_string_1 = '''
Register A: 0
Register B: 2024
Register C: 43690

Program: 4,0
'''

test_string_2 = '''
Register A: 2024
Register B: 0
Register C: 0

Program: 6,1,5,5
'''

test_string_3 = '''
Register A: 2024
Register B: 0
Register C: 0

Program: 7,1,5,6
'''

test_string_4 = '''
Register A: 2024
Register B: 0
Register C: 0

Program: 7,1,5,6
'''

test_input = test_string_3.split('\n')[1:-1]

registers, output = executer(input)

print(registers, ''.join([str(x) for x in output]))