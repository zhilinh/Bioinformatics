import sys

spectrum = {'G':57,
'A':71,
'S':87,
'P':97,
'V':99,
'T':101,
'C':103,
'I':113,
'L':113,
'N':114,
'D':115,
'K':128,
'Q':128,
'E':129,
'M':131,
'H':137,
'F':147,
'R':156,
'Y':163,
'W':186}

count = {}
lines = sys.stdin.read().splitlines()
gene = lines[0]
exp = lines[1].split()
l = len(gene)
mass = [0]
for i in range(l):
    mass.append(spectrum[gene[i]] + mass[i])
max = mass[-1]
linear = [0]
for i in range(l):
    for j in range(i + 1, l):
        linear.append(mass[j] - mass[i])
        linear.append(max - (mass[j] - mass[i]))
linear.sort()
linear.append(max)

score = 0
for i in linear:
    if not i in count:
        count[i] = [1, 0]
    else:
        count[i][0] += 1
for i in exp:
    if not int(i) in count:
        count[int(i)] = [0, 1]
    else:
        count[int(i)][1] += 1
for i in count:
    if count[i][0] <= count[i][1]:
        score += count[i][0]
    else:
        score += count[i][1]
print(score)