input: list[str] = list()

with open("input/day_21_test.txt", "r") as file:
    for line in file:
        input.append(line.rstrip())
        
def door_to_robot_translater(target_sequence: str) -> str:
    horisontal_pre = 0  #down is +1
    vertical_pre = 0    #right is +1
    horisontal_pos = 0
    vertical_pos = 0
    
    translation = ''
    last_target = 'A'
    
    for target_button in target_sequence:
        match target_button:
            case '0': 
                vertical_pre -= 1
                vertical_pos += 1
            case '1':
                horisontal_pre -= 1
                vertical_pre -= 2
                horisontal_pos += 1
                vertical_pos += 2
            case '2':
                horisontal_pre -= 1
                vertical_pre -= 1
                horisontal_pos += 1
                vertical_pos += 1
            case '3':
                horisontal_pre -= 1
                horisontal_pos += 1
            case '4':
                horisontal_pre -= 2
                vertical_pre -= 2
                horisontal_pos += 2
                vertical_pos += 2
            case '5':
                horisontal_pre -= 2
                vertical_pre -= 1
                horisontal_pos += 2
                vertical_pos += 1
            case '6':
                horisontal_pre -= 2
                horisontal_pos += 2
            case '7':
                horisontal_pre -= 3
                vertical_pre -= 2
                horisontal_pos += 3
                vertical_pos += 2
            case '8':
                horisontal_pre -= 3
                vertical_pre -= 1
                horisontal_pos += 3
                vertical_pos += 1
            case '9':
                horisontal_pre -= 3
                horisontal_pos += 3
            case 'A':
                horisontal_pos = 0
                vertical_pos = 0
    
        # Mixing is somehow optimal
        # we don't do mixing...   
        if last_target in ['0', 'A']:
            if horisontal_pre <= 0:
                translation = translation + '^'*(-horisontal_pre)
            
            if vertical_pre <= 0:
                translation = translation + '<'*(-vertical_pre)
        else:
            if vertical_pre <= 0:
                translation = translation + '<'*(-vertical_pre)
            
            if horisontal_pre <= 0:
                translation = translation + '^'*(-horisontal_pre)

        if vertical_pre > 0:
            translation = translation + '>'*vertical_pre

        if horisontal_pre > 0:
            translation = translation + 'v'*horisontal_pre
            
        
        translation = translation + 'A'
        
        horisontal_pre = horisontal_pos
        vertical_pre = vertical_pos
        
        horisontal_pos = 0
        vertical_pos = 0
        
    if horisontal_pre <= 0:
        translation = translation + '^'*(-horisontal_pre)
    
    if vertical_pre <= 0:
        translation = translation + '<'*(-vertical_pre)

    if vertical_pre > 0:
        translation = translation + '>'*vertical_pre

    if horisontal_pre > 0:
        translation = translation + 'v'*horisontal_pre
        
    last_target = target_button
        
    return translation

def robot_to_robot_translater(target_sequence: str) -> str:
    horisontal_pre = 0  #down is +1
    vertical_pre = 0    #right is +1
    horisontal_pos = 0
    vertical_pos = 0
    
    translation = ''
    
    for target_button in target_sequence:
        match target_button:
            case '>':
                horisontal_pre += 1
                horisontal_pos -= 1
            case '^':
                vertical_pre -= 1
                vertical_pos += 1
            case '<':
                horisontal_pre += 1
                vertical_pre -= 2
                horisontal_pos -= 1
                vertical_pos += 2
            case 'v':
                horisontal_pre += 1
                vertical_pre -= 1
                horisontal_pos -= 1
                vertical_pos += 1
            case 'A':
                horisontal_pos = 0
                vertical_pos = 0
        
        if horisontal_pre > 0:
            translation = translation + 'v'*horisontal_pre
    
        if vertical_pre <= 0:
            translation = translation + '<'*(-vertical_pre)

        if vertical_pre > 0:
            translation = translation + '>'*vertical_pre

        if horisontal_pre <= 0:
            translation = translation + '^'*(-horisontal_pre)
        
        translation = translation + 'A'
        
        horisontal_pre = horisontal_pos
        vertical_pre = vertical_pos
        
        horisontal_pos = 0
        vertical_pos = 0
        
    if horisontal_pre > 0:
        translation = translation + 'v'*horisontal_pre
    
    if vertical_pre <= 0:
        translation = translation + '<'*(-vertical_pre)
    
    if vertical_pre > 0:
        translation = translation + '>'*vertical_pre
        
    if horisontal_pre <= 0:
        translation = translation + '^'*(-horisontal_pre)
        
    return translation

complexity_sum = 0

for sequence in input:
    door_key = sequence[:-1]
    #print(int(door_key))
    door_robot = door_to_robot_translater(sequence)
    robot_1 = robot_to_robot_translater(door_robot)
    robot_2 = robot_to_robot_translater(robot_1)
    if sequence == '379A':
        print(sequence)
        print(door_robot)
        print(robot_1)
        print(robot_2)
    sequence_length = len(robot_2)
    #print(sequence_length)
    complexity = sequence_length*int(door_key)
    complexity_sum += complexity

print(complexity_sum)