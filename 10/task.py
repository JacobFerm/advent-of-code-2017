import operator
from util import hash

def get_string_input(input):
    return map(int,input.split(','))

input = "212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164"

hash1 = hash.sparse_hash(get_string_input(input), 1)
print "Part 1: " + str(hash1[0] * hash1[1])
print "Part 2: " + hash.knot_hash(input)