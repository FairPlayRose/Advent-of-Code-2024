import re
import math

input = list()

with open("input/day_14.txt", "r") as file:
    for line in file:
        input.append(re.search('p=(-*[0-9]+),(-*[0-9]+) v=(-*[0-9]+),(-*[0-9]+)', line).groups())

Y, X = 101, 103

robots_final_pos = [((int(pos_y) + 100 * int(speed_y)) % Y, (int(pos_x) + 100 * int(speed_x)) % X) for pos_y, pos_x, speed_y, speed_x in input]

#print(robots_final_pos)

Y_mid, X_mid = Y//2, X//2

#print(Y_mid, X_mid)

robot_quadrant_count = {'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0}

for robot_y, robot_x in robots_final_pos:
    if robot_y < Y_mid and robot_x < X_mid:
        robot_quadrant_count['Q1'] += 1
    if robot_y < Y_mid and robot_x > X_mid:
        robot_quadrant_count['Q2'] += 1
    if robot_y > Y_mid and robot_x < X_mid:
        robot_quadrant_count['Q3'] += 1
    if robot_y > Y_mid and robot_x > X_mid:
        robot_quadrant_count['Q4'] += 1

#print(robot_quadrant_count)

check_sum = 1
for quadrant in robot_quadrant_count.values():
    check_sum = check_sum * quadrant

print(check_sum)