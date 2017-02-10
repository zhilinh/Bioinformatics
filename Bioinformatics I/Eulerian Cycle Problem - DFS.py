import sys

def euler(start):
    global circuit, ava, step
    count = True
    circuit.append(str(start))
    if step == n:
        output = ''
        for i in circuit:
            output += i + '->'
        output = output[0 : len(output) - 2]
        print(output)
        exit()

    for i in edge[start]:
        if ava[(start, i)]:
            ava[(start, i)] = False
            count = False
            step += 1
            if not(euler(i)):
                count = True
                step -= 1
            ava[(start, i)] = True
    if count:
        circuit.pop(-1)
        return False

lines = sys.stdin.read().splitlines()
edge = []
circuit = []
n = 0
step = 0
ava = {}
for i in range(len(lines)):
    p = lines[i].split()
    p = p[2].split(',')
    edge.append([])
    for j in p:
        n += 1
        edge[i].append(int(j))
        ava[(i, int(j))] = True
euler(0)
