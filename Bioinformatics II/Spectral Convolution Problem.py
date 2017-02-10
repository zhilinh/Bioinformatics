import sys

count = {}
lines = sys.stdin.read().split()
for i in range(len(lines)):
    lines[i] = int(lines[i])
lines.sort()
for i in range(1, len(lines)):
    for j in range(i):
        k = lines[i] - lines[j]
        if k != 0:
            if k in count:
                count[k] += 1
            else:
                count[k] = 1
output = ''
for i in count:
    for j in range(count[i]):
        output += str(i) + ' '
print(output)