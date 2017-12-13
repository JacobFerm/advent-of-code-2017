import re
p = re.compile('(\d*) <-> (.*)')

def get_group(visited, connections, group_list, member):
    connected_members = connections[member]
    for connected_member in connected_members:        
        if connected_member not in group_list:
            group_list += [connected_member]
            visited[connected_member] = True
            get_group(visited, connections, group_list, connected_member)
    return group_list


def find_groups(connections):
    visited = [False] * len(connections)
    groups = []
    while False in visited:
        i = visited.index(False)
        groups += [len(get_group(visited, connections, [], i))]
    return groups

with open ('12/input.txt') as inputFile:
    input = inputFile.read()

connections = []
for line in input.splitlines():
    m = p.match(line)
    connections += [map(int, m.group(2).split(', '))]

groups = find_groups(connections)
print groups[0]
print len(groups)

