import sys

lines = sys.stdin.read().splitlines()
lines[1] = lines[1].split(',')
minnumcoins = [0]
lines[0] = int(lines[0])
for i in range(len(lines[1])):
    lines[1][i] = int(lines[1][i])
for i in range(1, lines[0] + 1):
    minnum = float('inf')
    for j in lines[1]:
        if i >= j:
            if minnumcoins[i - j] + 1 < minnum:
                minnum = minnumcoins[i - j] + 1
    minnumcoins.append(minnum)
print (minnumcoins[-1])
