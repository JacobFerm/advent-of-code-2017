import numpy as np

# Cube-based coordinate approach, see https://www.redblobgames.com/grids/hexagons/ for details.
MOVES = { 'n': np.array([1,0,-1]), 'ne': np.array([1,-1,0]), 'se': np.array([0,-1,1]), 's': np.array([-1,0,1]), 'sw': np.array([-1,1,0]), 'nw': np.array([0,1,-1]) }

def get_distance(pos):
    return max(abs(pos[0]), abs(pos[1]), abs(pos[2]))

with open ('11/input.txt') as inputFile:
    input = inputFile.read()

pos = np.array([0,0,0])
max_distance = 0
for move in input.split(','):
    pos += MOVES[move]
    max_distance = max(max_distance, get_distance(pos))

print get_distance(pos)
print max_distance
