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
innode = {}
outnode = {}
circuit = []
join = [0, 0]
max = 0
for i in range(len(lines)):
    p = lines[i].split()
    q = int(p[0])
    if q > max:
        max = q
    p = p[2].split(',')
    edge[q] = []
    outnode[q] = len(p)
    for j in p:
        edge[q].append(int(j))
        ava[(q, int(j))] = True
        if int(j) in innode:
            innode[int(j)] += 1
        else:
            innode[int(j)] = 1
for i in range(max + 1):
    if i in innode and i in outnode:
        if innode[i] < outnode[i]:
            join[1] = i
        elif innode[i] > outnode[i]:
            join[0] = i
    elif i in outnode and not i in innode:
        join[1] = i
    elif i in innode and not i in outnode:
        join[0] = i
ava[join[0], join[1]] = True
if join[0] in edge:
    edge[join[0]].append(join[1])
else:
    edge[join[0]] = [join[1]]
stack = [join[1]]
euler(join[1])
circuit = circuit[::-1]
circuit.pop(-1)
output = ''
input = ''
if not join[0] in outnode:
    for i in range(len(circuit)):
        input += str(circuit[i]) + '->'
        if circuit[i] == join[0]:
            for j in range(i + 1, len(circuit)):
                output += str(circuit[j]) + '->'
            output += input
            break
else:
    output = ''
    for i in circuit:
        output += str(i) + '->'
output = output[0 : len(output) - 2]
print(output)