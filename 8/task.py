import collections
import operator as op
Instruction = collections.namedtuple('Instruction', ['name', 'operator', 'value', 'target', 'condition', 'threshold'])
OPERATORS = { 'inc': op.add, 'dec': op.sub, '==': op.eq, '!=': op.ne, '<': op.lt, '>': op.gt, '<=': op.le, '>=': op.ge }

def map_to_instruction(line):
    a = line.split()
    return Instruction(a[0],OPERATORS[a[1]], int(a[2]), a[4], OPERATORS[a[5]], int(a[6]))

with open ('8/input.txt') as inputFile:
    input = inputFile.read()

max_value = 0
instructions = map(map_to_instruction, input.splitlines())
registers = dict.fromkeys(set(map(lambda x: x.name, instructions) + map(lambda x: x.target, instructions)), 0)

for instruction in instructions:
    if instruction.condition(registers[instruction.target], instruction.threshold):
        registers[instruction.name] = instruction.operator(registers[instruction.name], instruction.value)
        max_value = max(max_value, registers[instruction.name])

print max(registers.iteritems(), key=op.itemgetter(1))
print max_value

