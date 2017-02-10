import sys

chromosome = sys.stdin.read().split(')(')
for i in range(len(chromosome)):
    chromosome[i] = chromosome[i].split(' ')
chromosome[0][0] = chromosome[0][0][1:]
chromosome[-1][-1] = chromosome[-1][-1][:-2]
output = ''
for i in range(len(chromosome)):
    for j in range(len(chromosome[i])):
        chromosome[i][j] = int(chromosome[i][j])

"""[map(lambda x:int(x), chromosome[i]) for i in range(len(chromosome))]"""

for i in range(len(chromosome)):
    for j in range(len(chromosome[i]) - 1):
        if chromosome[i][j] > 0:
            m = 2 * chromosome[i][j]
        else:
            m = 2 * -chromosome[i][j] - 1
        if chromosome[i][j + 1] > 0:
            n = 2 * chromosome[i][j + 1] - 1
        else:
            n = 2 * -chromosome[i][j + 1]
        output += '(' + str(m) + ', ' + str(n) + '), '
    if chromosome[i][j + 1] > 0:
        m = 2 * chromosome[i][j + 1]
    else:
        m = 2 * -chromosome[i][j + 1] - 1
    if chromosome[i][0] > 0:
        n = 2 * chromosome[i][0] - 1
    else:
        n = 2 * -chromosome[i][0]
    output += '(' + str(m) + ', ' + str(n) + '), '
output = output[:-2]
print(output)
