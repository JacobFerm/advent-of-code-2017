def calc_jumps(input, calc_offset = lambda x: 1):
    instr = map(int, input.splitlines())
    pos = 0
    steps = 0
    while pos >= 0 and pos < len(instr):
        jump = instr[pos]
        instr[pos] += calc_offset(instr[pos])
        pos += jump
        steps += 1
    return steps

with open ('5/input.txt') as inputFile:
    input = inputFile.read()

print calc_jumps(input)
print calc_jumps(input, lambda x: -1 if x >= 3 else 1)