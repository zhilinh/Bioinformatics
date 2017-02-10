import sys
import math

line = sys.stdin.read().splitlines()
chromosome1 = line[0].split(')(')
for i in range(len(chromosome1)):
    chromosome1[i] = chromosome1[i].split(' ')
chromosome1[0][0] = chromosome1[0][0][1:]
chromosome1[-1][-1] = chromosome1[-1][-1][:-1]
max_val = 0
for i in range(len(chromosome1)):
    for j in range(len(chromosome1[i])):
        chromosome1[i][j] = int(chromosome1[i][j])
        if math.sqrt(chromosome1[i][j] ** 2) > max_val:
            max_val = int(math.sqrt(chromosome1[i][j] ** 2))
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

circles = 0
while edges1 != []:
    first = edges1[0][0]
    n = edges1[0][1]
    edges1.remove(edges1[0])
    while n != first:
        k = False
        for i in range(len(edges2)):
            for j in range(2):
                if edges2[i][j] == n:
                    if j == 0:
                        n = edges2[i][1]
                    else:
                        n = edges2[i][0]
                    edges2.remove(edges2[i])
                    k = True
                    break
            if k:
                break
        if n != first:
            k = False
            for i in range(len(edges1)):
                for j in range(2):
                    if edges1[i][j] == n:
                        if j == 0:
                            n = edges1[i][1]
                        else:
                            n = edges1[i][0]
                        edges1.remove(edges1[i])
                        k = True
                        break
                if k:
                    break
    circles += 1
print(max_val - circles)