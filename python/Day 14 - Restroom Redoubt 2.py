import re

input = list()

with open("input/day_14.txt", "r") as file:
    for line in file:
        input.append(re.search('p=(-*[0-9]+),(-*[0-9]+) v=(-*[0-9]+),(-*[0-9]+)', line).groups())

Y, X = 101, 103

robots_final_pos = [((int(pos_y) + 100 * int(speed_y)) % Y, (int(pos_x) + 100 * int(speed_x)) % X) for pos_y, pos_x, speed_y, speed_x in input]

#Solution for my input at 7520, also i somehow swaped X and Y, but don't know how...

for i in range(7520,7521):
    mat = [['.' for _ in range(X)] for _ in range(Y)]
    robot_pos = [((int(pos_y) + i * int(speed_y)) % Y, (int(pos_x) + i * int(speed_x)) % X) for pos_y, pos_x, speed_y, speed_x in input]
    for robot_y, robot_x in robot_pos:
        mat[robot_y][robot_x] = '#'

    string = ''.join([''.join(line) + '\n' for line in mat])
    with open("input/output.txt", "a") as f:
        print(i, file=f)
        print(string, file=f)

