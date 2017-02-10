import sys

line = sys.stdin.read().split(' ')
line[0] = line[0][1:]
line[-1] = line[-1][:-2]
n = len(line)
for i in range(n):
    line[i] = int(line[i])
if line[0] == 1:
    breakpoints = 0
else:
    breakpoints = 1
for i in range(1, n):
    if line[i] - line[i - 1] != 1:
        breakpoints += 1
print(breakpoints)