import sys
sys.setrecursionlimit(10000)#IMPORTANT!!!
#k(max) = 11

def euler(start):
    global circuit, stack, ava
    for i in info[start]:
        if ava[start, i]:
            ava[start, i] = False
            stack.append(edge[(start, i)])
            euler(i)
    circuit.append(stack[-1])
    stack.pop(-1)
    return

k = int(sys.stdin.read())
lines = []
info = {}
ava = {}
edge = {}
circuit = []
for i in range(2 ** k):
    j = bin(i)
    j = j[2 : len(j)]
    while len(j) < k:
        j = '0' + j
    lines.append(j)
for i in range(len(lines)):
    prefix = lines[i][0 : len(lines[i]) - 1]
    suffix = lines[i][1 : len(lines[i])]
    edge[(prefix, suffix)] = i
    if not prefix in info:
        info[prefix] = [suffix]
    else:
        info[prefix].append(suffix)
for i in range(len(lines)):
    prefix = lines[i][0 : len(lines[i]) - 1]
    for j in info[prefix]:
        ava[(prefix, j)] = True
prefix = lines[0][0 : len(lines[0]) - 1]
stack = [0]
euler(prefix)
circuit.pop(-1)
circuit = circuit[::-1]
output = lines[circuit[0]][0 : k - 1]
for i in range(0, len(circuit)):
    output += lines[circuit[i]][-1]
output = output[0 : len(output) - k + 1]
print(output)