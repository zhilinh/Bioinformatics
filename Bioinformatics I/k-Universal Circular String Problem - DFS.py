import sys
sys.setrecursionlimit(10000)#IMPORTANT!!!
#k(max) = 11

def euler(start):
    global circuit, ari, step
    for i in edge[start]:
        if ari[i]:
            ari[i] = False
            step += 1
            circuit.append(i)
            euler(i)
            circuit.pop(-1)
        elif step == 2 ** k:
            output = lines[circuit[0]]
            for j in range(1, len(circuit)):
                output += lines[circuit[j]][-1]
            print(output)
            exit()
    return

k = int(sys.stdin.read())
lines = []
info = {}
ari = []
edge = []
circuit = [0]
step = 1
for i in range(2 ** k):
    j = bin(i)
    j = j[2 : len(j)]
    while len(j) < k:
        j = '0' + j
    lines.append(j)
    ari.append(True)
for i in range(len(lines)):
    prefix = lines[i][0 : len(lines[i]) - 1]
    if not prefix in info:
        info[prefix] = [i]
    else:
        info[prefix].append(i)
for i in range(len(lines)):
    suffix = lines[i][1 : len(lines[i])]
    if suffix in info:
        edge.append(list(info[suffix]))
        if i in edge[-1]:
            edge[-1].remove(i)
ari[0] = False
euler(0)