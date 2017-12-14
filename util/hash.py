import operator

def reverse_list(hash_list, pos, length):
    temp_list = list(hash_list)
    for i in range(length):
        hash_list[(pos+i) % 256] = temp_list[(pos+length-1-i) % 256] 

def sparse_hash(input, rounds):
    hash_list = range(256)
    pos = 0
    skip = 0   

    for i in range(rounds):
        for length in input:
            reverse_list(hash_list, pos, length)
            pos += (length + skip) % 256
            skip += 1
        
    return hash_list

def dense_hash(input):
    spliced_list = [input[x:x+16] for x in range(0, 256, 16)]
    return map(lambda x: reduce(operator.xor, x), spliced_list)

def convert_to_hex(input):
    return ''.join(map(lambda x: format(x, '02x'), input))

def get_byte_input(input):
    return [ord(c) for c in input] + [17, 31, 73, 47, 23]

def knot_hash(input):
    sparse = sparse_hash(get_byte_input(input), 64)
    dense = dense_hash(sparse)
    return convert_to_hex(dense)
