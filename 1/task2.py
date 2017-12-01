with open ('1/input.txt') as inputFile:
    input = inputFile.read()

result = 0
length = len(input)
for x in range(0, length):
    if input[x] == input[(x+length/2) % length]:
        result += int(input[x])

print result
