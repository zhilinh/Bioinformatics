import sys

lines = sys.stdin.read().splitlines()
k = int(lines[0])
string1 = lines[1]
string2 = lines[2]
kmers = {}
rc = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
for i in range(len(string1) - k + 1):
    kmer = string1[i : i + k]
    rc_kmer = ''
    for j in kmer:
        rc_kmer = rc[j] + rc_kmer
    if not kmer in kmers:
        kmers[kmer] = [i]
    else:
        kmers[kmer].append(i)
    if not rc_kmer in kmers:
        kmers[rc_kmer] = [i]
    else:
        kmers[rc_kmer].append(i)

for i in range(len(string2) - k + 1):
    kmer = string2[i : i + k]
    if kmer in kmers:
        for j in kmers[kmer]:
            print('(' + str(j) + ', ' + str(i) + ')')