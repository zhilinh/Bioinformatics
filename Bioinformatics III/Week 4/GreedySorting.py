import sys

def greedysorting(m, line):
    global n, output
    output_copy = output
    if m == n + 1:
        return
    for i in range(n):
        if line[i] == m or line[i] == -m:
            line[:i + 1] = line[0:i + 1][::-1]
            for j in range(i + 1):
                line[j] = -line[j]
            k = len(output)
            for j in line:
                if j > 0:
                    output_copy += '+' + str(j) + ' '
                else:
                    output_copy += str(j) + ' '
            output_copy = output_copy[:-1] + ')'
            print(output_copy)
            if line[0] == -m:
                line[0] = m
                output_copy = output + '+' + output_copy[k + 1:]
                print(output_copy)
            output += '+' + str(line[0]) + ' '
            greedysorting(m + 1, line[1:])
            break
    return

line = sys.stdin.read().split(' ')
line[0] = line[0][1:]
line[-1] = line[-1][:-2]
n = len(line)
output = '('
for i in range(n):
    line[i] = int(line[i])
greedysorting(1, line)