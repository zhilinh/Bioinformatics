import sys

lines = sys.stdin.read().splitlines()
chromosome1 = lines[0].split(')(')
iijj = lines[1].split(', ')
for i in range(4):
    iijj[i] = int(iijj[i])
for i in range(len(chromosome1)):
    chromosome1[i] = chromosome1[i].split(' ')
chromosome1[0][0] = chromosome1[0][0][1:]
chromosome1[-1][-1] = chromosome1[-1][-1][:-1]
for i in range(len(chromosome1)):
    for j in range(len(chromosome1[i])):
        chromosome1[i][j] = int(chromosome1[i][j])

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

for i in range(len(edges1)):
    if edges1[i] == (iijj[0], iijj[1]) or edges1[i] == (iijj[1], iijj[0]):
        if edges1[i][0] == iijj[0]:
            edges1[i] = (iijj[0], iijj[2])
        else:
            edges1[i] = (iijj[1], iijj[3])
    elif edges1[i] == (iijj[2], iijj[3]) or edges1[i] == (iijj[3], iijj[2]):
        if edges1[i][0] == iijj[2]:
            edges1[i] = (iijj[2], iijj[0])
        else:
            edges1[i] = (iijj[3], iijj[1])

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
            edges1.remove(edges1[i])
output = output[:-1]
print(output)