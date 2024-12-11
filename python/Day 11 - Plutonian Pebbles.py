from functools import cache

'''
As you observe them for a while, you find that the stones have a consistent behavior. 
Every time you blink, the stones each simultaneously change according to the first applicable rule in this list:

1.  If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.

2.  If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
    The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. 
    (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)

3.  If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
'''

input = list()

with open("input/day_11.txt", "r") as file:
    for line in file:
        input.append(line.rstrip().split(' '))

input = [int(x) for x in input[0]]

#print(input)

@cache
def substones(stone: int, step: int, end: int) -> int:
    if step == end:
        return 1

    if stone == 0:
        return substones(1, step + 1, end)
    elif len(str(stone)) % 2 == 0:
        left, right = int(str(stone)[:len(str(stone))//2]), int(str(stone)[len(str(stone))//2 :])
        return sum([substones(left, step + 1, end), substones(right, step + 1, end)])
    else:
        return substones(stone*2024, step + 1, end)

#Part 1
#print(sum([substones(stone, 0, 25) for stone in input]))

#Part 2
#Remember tail recursion optimisation with cache decorator
print(sum([substones(stone, 0, 75) for stone in input]))