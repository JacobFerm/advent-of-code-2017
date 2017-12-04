import math
import numpy as np

np.set_printoptions(linewidth=200)
np.set_printoptions(threshold=np.nan)

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

def check_edge(input, start, n):
    if input >= start and input < start+n+1:
        steps = abs(start + (n+1)/2 - input)
        return n / 2 + 1 + steps
    else:
        return 0

def calc_steps(input):
    n = int(math.sqrt(input))
    n = n + (n%2-1)
    start = n*n

    if start == input: 
        return 2*n - 2

    steps = 0
    steps += check_edge(input, start, n)
    for _ in range(3):    
        start += n+1
        steps += check_edge(input, start, n)
    return steps

def calc_value(matrix, x, y):    
    return sum(sum(matrix[y-1:y+2, x-1:x+2]))

def calc_new_position(matrix, x, y, dir):
    if dir == RIGHT:
        if matrix[y-1][x] == 0:
            y -= 1
            dir = UP
        else:
            x += 1
    elif dir == UP:
        if matrix[y][x-1] == 0:
            x -= 1
            dir = LEFT
        else:
            y -= 1
    elif dir == LEFT:
        if matrix[y+1][x] == 0:
            y += 1
            dir = DOWN
        else:
            x -= 1
    elif dir == DOWN:
        if matrix[y][x+1] == 0:
            x += 1
            dir = RIGHT
        else:
            y += 1
    return x,y,dir

def calc_steps2(input):
    n = 15
    matrix = np.zeros((n,n), dtype=np.int)
    x = y = 7
    value = 1
    dir = DOWN
    matrix[y][x] = value

    while value <= input:
        x,y,dir = calc_new_position(matrix,x,y,dir)
        value = calc_value(matrix,x,y)
        matrix[y][x] = value

    print matrix
    return value

print calc_steps(361527)
print calc_steps2(361527)