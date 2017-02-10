import sys

lines= sys.stdin.read().splitlines()
chromosome1 = lines[0].split('), (')
iijj = lines[1].split(', ')
for i in range(len(chromosome1)):
    chromosome1[i] = chromosome1[i].split(', ')
chromosome1[0][0] = chromosome1[0][0][1:]
chromosome1[-1][-1] = chromosome1[-1][-1][:-1]
for i in range(4):
    iijj[i] = int(iijj[i])
for i in range(len(chromosome1)):
    for j in range(len(chromosome1[i])):
        chromosome1[i][j] = int(chromosome1[i][j])
if [iijj[0], iijj[1]] in chromosome1:
    chromosome1.remove([iijj[0], iijj[1]])
elif [iijj[1], iijj[0]] in chromosome1:
    chromosome1.remove([iijj[1], iijj[0]])
if [iijj[2], iijj[3]] in chromosome1:
    chromosome1.remove([iijj[2], iijj[3]])
elif [iijj[3], iijj[2]] in chromosome1:
    chromosome1.remove([iijj[3], iijj[2]])
chromosome1.append([iijj[0], iijj[2]])
chromosome1.append([iijj[1], iijj[3]])
output = ''
for i in range(len(chromosome1)):
    output +=  str(tuple(chromosome1[i])) + ', '
output = output[:-2]
print(output)