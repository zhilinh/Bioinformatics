import sys

lines = sys.stdin.read().splitlines()
seq1 = lines[0]
seq2 = lines[1]
s = [[0]]
for i in range(len(seq1)):
    s.append([-1 * (i + 1)])
for j in range(len(seq2)):
    s[0].append(-1 * (j + 1))
for i in range(1, len(seq1) + 1):
    for j in range(1, len(seq2) + 1):
        same = -1
        if seq1[i - 1] == seq2[j - 1]:
            same = 0
        s[i].append(max((s[i][j - 1] - 1, s[i - 1][j] - 1, s[i - 1][j - 1] + same)))
print(-s[-1][-1])