import sys

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
ava = {}
edge = {}
circuit = []
for i in range(len(lines)):
    p = lines[i].split()
    q = int(p[0])
    p = p[2].split(',')
    edge[q] = []
    for j in p:
        edge[q].append(int(j))
        ava[(q, int(j))] = True
stack = [0]
euler(0)
circuit = circuit[::-1]
output = ''
for i in circuit:
    output += str(i) + '->'
output = output[0 : len(output) - 2]
print(output)