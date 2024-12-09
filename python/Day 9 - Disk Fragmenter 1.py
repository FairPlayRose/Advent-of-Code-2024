input = list()

with open("input/day_09.txt", "r") as file:
    for line in file:
        input.append(line.rstrip())

def fileDiskMaker(data: str) -> list[int|str]:

    char_list = list()

    for index, char in enumerate(data):
        for _ in range(int(char)):
            if index % 2 == 1:
                char_list.append('.')
            else:
                char_list.append(index//2)
    return char_list

input = input[0]

#print(input)
disk_format = fileDiskMaker(input)
disk_format_rev = list(reversed(disk_format))
disk_len = len(disk_format)
#print(disk_format)

right_meet_left = False
left_index = 0
right_index = 0

check_sum = 0

while right_meet_left == False:
    #print(left_index, right_index)
    if left_index + right_index >= disk_len:
        right_meet_left == True
        break

    #print(disk_format[left_index], not disk_format[left_index] == '.', disk_format_rev[right_index], not disk_format_rev[right_index] == '.')
    
    if not disk_format[left_index] == '.':
        check_sum += disk_format[left_index]*(left_index )
        left_index += 1
    elif not disk_format_rev[right_index] == '.':
        check_sum += disk_format_rev[right_index]*(left_index)
        left_index += 1
        right_index += 1
    else:
        right_index += 1
    


print(check_sum)

        