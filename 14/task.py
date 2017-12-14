from util import hash
import numpy

def check_square(squares, x, y):
    if x < 0 or x > 127 or y < 0 or y > 127 or squares[y][x] == 0:
        return False
    else:
        squares[y][x] = 0
        check_square(squares, x-1, y)
        check_square(squares, x+1, y)
        check_square(squares, x, y-1)
        check_square(squares, x, y+1)
        return True

def count_regions(binary_strings):
    squares = map(lambda x: map(int, x), binary_strings)
    print squares
    regions = 0
    for i in range(128):
        for j in range(128):
            if check_square(squares, i, j):
                regions += 1
    return regions

input = 'oundnydw'

disk = map(lambda x: input + "-" + str(x), range(128))
hashes = map(hash.knot_hash, disk)
binary_strings = map(lambda x: format(int(x, 16), '0128b'), hashes)

used_squares = sum(map(lambda x: x.count('1'), binary_strings))
print used_squares

regions = count_regions(binary_strings)
print regions

