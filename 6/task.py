with open ('6/input.txt') as inputFile:
    input = inputFile.read()

banks = map(int, input.split())
configurations = []
while True:
    index = banks.index(max(banks))
    blocks = banks[index]
    banks[index] = 0
    while blocks > 0:
        index = (index + 1) % len(banks)
        banks[index] += 1
        blocks -= 1
    if banks in configurations:
        break
    else:
        configurations.append(list(banks))
print "Configurations before cycle detected: " + str(len(configurations) + 1)
print "Length of cycle: " + str(len(configurations) - configurations.index(banks))