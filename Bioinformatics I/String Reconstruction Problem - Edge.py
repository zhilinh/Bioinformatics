import sys
sys.setrecursionlimit(10000)#IMPORTANT!!!

def euler(start):
    global circuit, stack, ava
    for i in edge[start]:
        if ava[start, i]:
            ava[start, i] = False
            stack.append(i)
            euler(i)
    circuit.append(stack[-1])
    stack.pop(-1)
    return

lines = sys.stdin.read().splitlines()
lines.pop(0)
info = {}
ava = {}
edge = []
suffix_set = []
circuit = []
join = [0, 0]
for i in range(len(lines)):
    prefix = lines[i][0 : len(lines[i]) - 1]
    suffix_set.append(lines[i][1 : len(lines[i])])
    if not prefix in info:
        info[prefix] = [i]
    else:
        info[prefix].append(i)

for i in range(len(lines)):
    prefix = lines[i][0 : len(lines[i]) - 1]
    suffix = lines[i][1 : len(lines[i])]
    if suffix in info:
        edge.append(info[suffix])
        for j in info[suffix]:
            ava[(i, j)] = True
    else:
        join[1] = i
        edge.append([])
    if not prefix in suffix_set:
        join[0] = i
edge[join[1]] = [join[0]]
ava[join[1], join[0]] = True
stack = [join[0]]
euler(join[0])
circuit = circuit[::-1]
circuit.pop(-1)
output = lines[circuit[0]]
for i in range(1, len(circuit)):
    output += lines[circuit[i]][-1]
print(output)