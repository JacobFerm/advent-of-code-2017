def calculate_captcha(input, lookahead):
    result = 0
    length = len(input)
    for i in range(0, length):
        if input[i] == input[(i+lookahead) % length]:
            result += int(input[i])
    return result

with open ('1/input.txt') as inputFile:
    input = inputFile.read()

print calculate_captcha(input, 1)
print calculate_captcha(input, len(input)/2)