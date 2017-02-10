import sys

line = sys.stdin.read().split(' ')
line[0] = line[0][1:]
line[-1] = line[-1][:-2]
n = len(line)
output = '('
for i in range(n):
    line[i] = int(line[i])
n = n // 2
for i in range(1, n + 1):
    if line[2 * i - 1] > line[2 * i - 2]:
        output += '+' + str(line[2 * i - 1] // 2) + ' '
    else:
        output += '-' + str(line[2 * i - 2] // 2) + ' '
output = output[:-1] + ')'
print(output)