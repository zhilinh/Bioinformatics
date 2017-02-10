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
gene = input()
l = len(gene)
mass = [0]
for i in range(l):
    mass.append(spectrum[gene[i]] + mass[i])
for i in range(1, l):
    for j in range(i, l):
        mass.append(mass[j + 1] - mass[i])
mass.sort()
output = ''
for i in mass:
    output += str(i) + ' '
print(output)