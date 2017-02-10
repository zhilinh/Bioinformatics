import sys

lines = sys.stdin.read().splitlines()
k = len(lines[0]) - 1
prefix = []
suffix = []
lines.sort()
for i in range(len(lines)):
    prefix.append(lines[i][0 : k])
    suffix.append(lines[i][1 : k + 1])
for i in range(len(lines)):
    for j in range(len(lines)):
        if suffix[i] == prefix[j]:
            print(lines[i], '->', lines[j])