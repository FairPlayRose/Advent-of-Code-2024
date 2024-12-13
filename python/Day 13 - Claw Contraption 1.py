from functools import cache
import re

input = list()
input_long = ''

#https://stackoverflow.com/questions/5929107/decorators-with-parameters

with open("input/day_13.txt", "r") as file:
    for line in file:
        input.append(line)

input_long = ''.join(input)
cranes = input_long.split("\n\n")
cranes = [list(re.search("Button A: X\+([0-9]+), Y\+([0-9]+)\\nButton B: X\+([0-9]+), Y\+([0-9]+)\\nPrize: X=([0-9]+), Y=([0-9]+)", crane).groups())
          for crane in cranes]
cranes = [[int(x) for x in crane] for crane in cranes]

#print(cranes)

@cache
def recursiveCranegame(pos: tuple[int,int], steps: tuple[int,int], A_X, A_Y, B_X, B_Y, T_X, T_Y, price: tuple[int,int]) -> tuple[int,int]:
    
    pos_x, pos_y = pos
    A_step, B_step = steps
    A_price, B_price = price

    if pos == (T_X, T_Y):
        return A_step*A_price + B_step*B_price
    if pos_x > T_X or pos_y > T_Y:
        return float('inf')
    if A_step >= 100 or B_step >= 100:
        return float('inf')
    
    A_recurtion = recursiveCranegame((pos_x+A_X, pos_y+A_Y), (A_step+1,B_step), A_X, A_Y, B_X, B_Y, T_X, T_Y, price)
    B_recurtion = recursiveCranegame((pos_x+B_X, pos_y+B_Y), (A_step,B_step+1), A_X, A_Y, B_X, B_Y, T_X, T_Y, price)

    return min(A_recurtion, B_recurtion)

#A_X, A_Y, B_X, B_Y, T_X, T_Y = cranes[0]
#print(A_X, A_Y, B_X, B_Y, T_X, T_Y)
#print(recursiveCranegame((0,0), (0,0), A_X, A_Y, B_X, B_Y, T_X, T_Y, (3,1)))
price_to_prize = [recursiveCranegame((0,0), (0,0), A_X, A_Y, B_X, B_Y, T_X, T_Y, (3,1)) for A_X, A_Y, B_X, B_Y, T_X, T_Y in cranes]
print(sum([price_of_prize for price_of_prize in price_to_prize if price_of_prize != float('inf')]))
