import sys

lines = sys.stdin.read().splitlines()
for i in range(len(lines)):
    lines[i] = lines[i].split()
n = int(lines[0][0])
m = int(lines[0][1])
down = [[]]
for i in range(1, n + 1):
    for j in lines[i]:
        down[i - 1].append(int(j))
    down.append([])
down.pop(-1)
right = [[]]
for i in range(n + 2, 2 * n + 3):
    for j in lines[i]:
        right[i - n - 2].append(int(j))
    right.append([])
right.pop(-1)

s = [[0]]
for i in range(1, n + 1):
    s.append([s[i - 1][0] + down[i - 1][0]])
for j in range(1, m + 1):
    s[0].append(s[0][j - 1] + right[0][j - 1])
for i in range(1, n + 1):
    for j in range(1, m + 1):
        s[i].append(max(s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1]))
print(s[n][m])