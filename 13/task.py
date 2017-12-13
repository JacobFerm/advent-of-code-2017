def create_firewall(input):
    firewall = {}
    for line in input.splitlines():
        stuff = line.split(': ')
        firewall[int(stuff[0])] = int(stuff[1])
    return firewall

def calc_severity(firewall, time):
    severity = 0
    for i in range(100):
        if i in firewall.keys() and (i+time) % (firewall[i] * 2 - 2) == 0:
            severity += i * firewall[i]    
    return severity

def check_firewall(firewall, time):
    for i in range(100):
        if i in firewall.keys() and (i+time) % (firewall[i] * 2 - 2) == 0:
            return False
    return True

def find_shortest_delay(firewall):
    t = 0
    while True:
        if check_firewall(firewall, t):
            break
        t += 1    
    return t

with open ('13/input.txt') as inputFile:
    input = inputFile.read()

firewall = create_firewall(input)

print calc_severity(firewall, 0)
print find_shortest_delay(firewall)


