import sys

def breakpointgraph(edges1, edges2):
    global iijj
    iijj = [0, 0, 0, 0]
    for i in range(len(edges1)):
        k = True
        kk = False
        for j in range(len(edges2)):
            if (edges1[i][0] == edges2[j][1] and edges1[i][1] == edges2[j][0]) or (edges1[i] == edges2[j]):
                k = False
                break
            else:
                kk = True
        if k and kk:
            iijj[2] = edges2[j][0]
            iijj[1] = edges2[j][1]
            return True

def output_edges(edges1):
    output = '('
    start = edges1[0]
    first = edges1[0]
    while edges1 != []:
        if first[1] % 2 == 0:
            j = True
        else:
            j = False
        if j:
            if first[1] - 1 == start[0]:
                output += '-' + str(first[1] // 2) + ')('
                edges1.remove(start)
                if edges1 == []:
                    break
                else:
                    start = edges1[0]
                    first = edges1[0]
            else:
                for i in range(len(edges1)):
                    if edges1[i][0] == first[1] - 1:
                        output += '-' + str(first[1] // 2) + ' '
                        first = edges1[i]
                        break
                    elif edges1[i][1] == first[1] - 1:
                        output += '-' + str(first[1] // 2) + ' '
                        first = (edges1[i][1], edges1[i][0])
                        break
                edges1.remove(edges1[i])
        else:
            if first[1] + 1 == start[0]:
                output += '+' + str((first[1] + 1) // 2) + ')('
                edges1.remove(start)
                if edges1 == []:
                    break
                else:
                    start = edges1[0]
                    first = edges1[0]
            else:
                for i in range(len(edges1)):
                    if edges1[i][0] == first[1] + 1:
                        output += '+' + str((first[1] + 1) // 2) + ' '
                        first = edges1[i]
                        break
                    elif edges1[i][1] == first[1] + 1:
                        output += '+' + str((first[1] + 1) // 2) + ' '
                        first = (edges1[i][1], edges1[i][0])
                        break
                edges1.remove(edges1[i])
    output = output[:-1]
    if output != '':
        print(output)

line = sys.stdin.read().splitlines()
chromosome1 = line[0].split(')(')
for i in range(len(chromosome1)):
    chromosome1[i] = chromosome1[i].split(' ')
chromosome1[0][0] = chromosome1[0][0][1:]
chromosome1[-1][-1] = chromosome1[-1][-1][:-1]
for i in range(len(chromosome1)):
    for j in range(len(chromosome1[i])):
        chromosome1[i][j] = int(chromosome1[i][j])
chromosome2 = line[1].split(')(')
for i in range(len(chromosome2)):
    chromosome2[i] = chromosome2[i].split(' ')
chromosome2[0][0] = chromosome2[0][0][1:]
chromosome2[-1][-1] = chromosome2[-1][-1][:-1]
for i in range(len(chromosome2)):
    for j in range(len(chromosome2[i])):
        chromosome2[i][j] = int(chromosome2[i][j])

edges1 = []
for i in range(len(chromosome1)):
    for j in range(len(chromosome1[i]) - 1):
        if chromosome1[i][j] > 0:
            m = 2 * chromosome1[i][j]
        else:
            m = 2 * -chromosome1[i][j] - 1
        if chromosome1[i][j + 1] > 0:
            n = 2 * chromosome1[i][j + 1] - 1
        else:
            n = 2 * -chromosome1[i][j + 1]
        edges1.append((m,n))
    if chromosome1[i][j + 1] > 0:
        m = 2 * chromosome1[i][j + 1]
    else:
        m = 2 * -chromosome1[i][j + 1] - 1
    if chromosome1[i][0] > 0:
        n = 2 * chromosome1[i][0] - 1
    else:
        n = 2 * -chromosome1[i][0]
    edges1.append((m, n))
edges2 = []
for i in range(len(chromosome2)):
    for j in range(len(chromosome2[i]) - 1):
        if chromosome2[i][j] > 0:
            m = 2 * chromosome2[i][j]
        else:
            m = 2 * -chromosome2[i][j] - 1
        if chromosome2[i][j + 1] > 0:
            n = 2 * chromosome2[i][j + 1] - 1
        else:
            n = 2 * -chromosome2[i][j + 1]
        edges2.append((m, n))
    if chromosome2[i][j + 1] > 0:
        m = 2 * chromosome2[i][j + 1]
    else:
        m = 2 * -chromosome2[i][j + 1] - 1
    if chromosome2[i][0] > 0:
        n = 2 * chromosome2[i][0] - 1
    else:
        n = 2 * -chromosome2[i][0]
    edges2.append((m, n))

nt_edges1 = edges1[:]
nt_edges2 = edges2[:]
output_edges(edges1[:])
while breakpointgraph(nt_edges1, nt_edges2):
    for i in range(len(edges1)):
        if edges1[i][1] == iijj[2]:
            iijj[0] = edges1[i][0]
            break
        elif edges1[i][0] == iijj[2]:
            iijj[0] = edges1[i][1]
            break
    edges1.remove(edges1[i])
    for j in range(len(edges1)):
        if edges1[j][0] == iijj[1]:
            iijj[3] = edges1[j][1]
            break
        elif edges1[j][1] == iijj[1]:
            iijj[3] = edges1[j][0]
            break
    edges1.remove(edges1[j])
    edges1.append((iijj[3], iijj[0]))
    edges1.append((iijj[2], iijj[1]))
    nt_edges1 = edges1[:]
    for i in range(len(edges1)):
        if edges1[i] in edges2:
            if edges1[i] in nt_edges2:
                nt_edges2.remove(edges1[i])
            nt_edges1.remove(edges1[i])
        elif (edges1[i][1], edges1[i][0]) in edges2:
            nt_edges1.remove(edges1[i])
            if (edges1[i][1], edges1[i][0]) in nt_edges2:
                nt_edges2.remove((edges1[i][1], edges1[i][0]))
    output_edges(edges1[:])