import sys

line = sys.stdin.read().split(' ')
line[0] = line[0][1:]
line[-1] = line[-1][:-2]
n = len(line)
node = []
output = '('
for i in range(n):
    line[i] = int(line[i])
for i in range(n):
    if line[i] > 0:
        node.append(2 * line[i] - 1)
        node.append(2 * line[i])
    else:
        node.append(2 * -line[i])
        node.append(2 * -line[i] - 1)
for i in range(len(node)):
    output += str(node[i]) + ' '
output = output[:-1] + ')'
print(output)