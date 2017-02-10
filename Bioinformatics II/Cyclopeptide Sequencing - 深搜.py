import sys

def cyclospectrum(peptides):
    spectrum = [0]
    l = len(peptides)
    for i in range(l):
        spectrum.append(peptides[i] + spectrum[i])
    max = spectrum[-1]
    linear = [0]
    for i in range(l):
        for j in range(i + 1, l):
            linear.append(spectrum[j] - spectrum[i])
            linear.append(max - (spectrum[j] - spectrum[i]))
    linear.sort()
    linear.append(max)
    return linear
def expand(peptides):
    global final
    for i in basic:
        peptides.append(i)
        count = 0
        for j in peptides:
            count += j
        if count == mass2[-1]:
            if cyclospectrum(peptides) == mass2:
                output = ''
                for j in peptides:
                    output += str(j) + '-'
                output = output[0 : len(output) - 1]
                final += output + ' '
        elif count in mass2:
            expand(peptides)
        peptides.pop(-1)
    return
table = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
mass1 = sys.stdin.read().split()
mass2 = []
peptides = []
basic = []
final = ''
for i in mass1:
    mass2.append(int(i))
for i in table:
    if i in mass2:
        basic.append(i)
expand(peptides)
final = final[0 : len(final) - 1]
print(final)