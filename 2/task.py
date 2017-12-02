import numpy as np

def calculate_diff_checksum(numbers):
    return max(numbers) - min(numbers)

def calculate_div_checksum(numbers):
    result = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j: continue
            if numbers[i] > numbers[j] and numbers[i] % numbers[j] == 0:
                result += numbers[i] / numbers[j]
    return result

def calculate_div_checksum2(numbers):
    mask = np.mod.outer(numbers, numbers) == 0
    np.fill_diagonal(mask, False)
    div = np.divide.outer(numbers, numbers)
    return sum(sum(mask * div))

def transform_to_int(line):
    return map(int, line.split())

def do_stuff(input, checksum_method):
    lines = map(transform_to_int, input.splitlines())
    checksums = map(checksum_method, lines)
    return sum(checksums)

with open ('2/input.txt') as inputFile:
    input = inputFile.read()

print do_stuff(input, calculate_diff_checksum)
print do_stuff(input, calculate_div_checksum)
print do_stuff(input, calculate_div_checksum2)