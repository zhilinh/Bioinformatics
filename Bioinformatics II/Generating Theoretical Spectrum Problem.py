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
max = mass[-1]
linear = [0]
#the keypoint is that it add one more list to stroage the result of every subtraction,
# because all results are generated from the exsiting list.

for i in range(l):
    for j in range(i + 1, l):
        linear.append(mass[j] - mass[i])
        linear.append(max - (mass[j] - mass[i]))
        #to solve the cyclic problem,
        # it is only needed to make the whole mass subtract every subpeptides' mass we generated.

linear.sort()
linear.append(max)
output = ''
for i in linear:
    output += str(i) + ' '
print(output)