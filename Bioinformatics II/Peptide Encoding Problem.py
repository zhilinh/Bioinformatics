import sys

replica = {'A':'T',
           'C':'G',
           'G':'C',
           'T':'A'}
dogma = {'AAA':'K',
'AAC':'N',
'AAG':'K',
'AAT':'N',
'ACA':'T',
'ACC':'T',
'ACG':'T',
'ACT':'T',
'AGA':'R',
'AGC':'S',
'AGG':'R',
'AGT':'S',
'ATA':'I',
'ATC':'I',
'ATG':'M',
'ATT':'I',
'CAA':'Q',
'CAC':'H',
'CAG':'Q',
'CAT':'H',
'CCA':'P',
'CCC':'P',
'CCG':'P',
'CCT':'P',
'CGA':'R',
'CGC':'R',
'CGG':'R',
'CGT':'R',
'CTA':'L',
'CTC':'L',
'CTG':'L',
'CTT':'L',
'GAA':'E',
'GAC':'D',
'GAG':'E',
'GAT':'D',
'GCA':'A',
'GCC':'A',
'GCG':'A',
'GCT':'A',
'GGA':'G',
'GGC':'G',
'GGG':'G',
'GGT':'G',
'GTA':'V',
'GTC':'V',
'GTG':'V',
'GTT':'V',
'TAA':'*',
'TAC':'Y',
'TAG':'*',
'TAT':'Y',
'TCA':'S',
'TCC':'S',
'TCG':'S',
'TCT':'S',
'TGA':'*',
'TGC':'C',
'TGG':'W',
'TGT':'C',
'TTA':'L',
'TTC':'F',
'TTG':'L',
'TTT':'F'}
lines = sys.stdin.read().splitlines()
k = len(lines[1]) * 3
for i in range(len(lines[0]) - k):
    pattern = lines[0][i : i + k]
    trans = ''
    for j in range(k // 3):
        codon = pattern[j * 3 : j * 3 + 3]
        if dogma[codon] == '*':
            break
        else:
            trans += dogma[codon]
    if trans == lines[1]:
        print(pattern)
    else:
        pattern = pattern[::-1]
        rc = ''
        trans = ''
        for j in range(k):
            for l in replica:
                if l == pattern[j]:
                    rc += replica[l]
        for j in range(k // 3):
            codon = rc[j * 3 : j * 3 + 3]
            if dogma[codon] == '*':
                break
            else:
                trans += dogma[codon]
        if trans == lines[1]:
            print(pattern[::-1])
