input = list()

with open("input/day_09_test.txt", "r") as file:
    for line in file:
        input.append(line.rstrip())

input = input[0]

input = [int(i) for i in input]
input = [['data' if index % 2 == 0 else 'break', index//2, num]
         for index, num in enumerate(input)]

rev_input = reversed(input)

print(input)

right_meet_left = False
left_index = 0
right_index = 0

break_space = list()
disk_space = 0

check_sum = 0

while right_meet_left == False:
    #print(left_index, right_index)
    if left_index + right_index >= len(input):
        right_meet_left == True
        break

    message, file_index, size = input[left_index]
    if message == 'data':
        for disk_index in range(disk_space, disk_space + size):
            check_sum += disk_index*file_index
        disk_space += size
        left_index += 1
    if message == 'break':
        break_space.append(size)
        message2, index2, size2 = rev_input[right_index]
        if message2 == 'data':
            for space in break_space:
                if size2 < space:
                    pass
                    
        

#print(check_sum)
