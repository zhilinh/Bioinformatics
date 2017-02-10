import sys

line = sys.stdin.read().split(', ')
line[-1] = line[-1][:-1]
edge = []
for i in range(len(line) // 2):
    line[i * 2] = line[i * 2][1:]
    line[i * 2 + 1] = line[i * 2 + 1][:-1]
    edge.append((int(line[i * 2]), int(line[i * 2 + 1])))

output = '('
mark = 0
for i in range(len(edge)):
    if edge[i][0] % 2 == 0:
        output += '+' + str(edge[i][0] // 2) + ' '
    else:
        output += '-' + str((edge[i][0] + 1) // 2) + ' '
    if (edge[i][1] == edge[mark][0] + 1 or edge[i][1] == edge[mark][0] - 1) and (i != mark):
        output = output[:-1] + ')('
        mark = i + 1
output = output[:-1]
print(output)