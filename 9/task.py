index = 0
score = 0
garbage = 0

def trim_garbage():
    global index, garbage, input
    while index < len(input):
        index += 1
        if input[index] == '!':
            index += 1
        elif input[index] == '>':
            return
        else:
            garbage += 1

def calc_group_score(level):
    global index, score, input
    while index < len(input):
        index += 1
        if input[index] == '}':
            score += level
            return
        elif input[index] == '{':
            calc_group_score(level+1)
        elif input[index] == '<':
            trim_garbage()
            
with open ('9/input.txt') as inputFile:
    input = inputFile.read()

calc_group_score(1)
print "score: " + str(score)
print "garbage: " + str(garbage)