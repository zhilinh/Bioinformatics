import sys
import random

def sc(matrix):
    n = len(matrix)
    o = 0
    for i in range(0, k):
        max = 0
        count = [0, 0, 0, 0]
        for j in range(0, n):
            if matrix[j][i : i + 1] == 'A':
                count[0] += 1
            elif matrix[j][i : i + 1] == 'C':
                count[1] += 1
            elif matrix[j][i : i + 1] == 'G':
                count[2] += 1
            else:
                count[3] += 1
        for j in range(0, 4):
            if count[j] > max:
                max = count[j]
        o += (n - max)
    return o

def pr(motifs):
    global a, c, g, t
    a = []
    c = []
    g = []
    t = []
    for i in range(0, k):
        a.append(1)
        c.append(1)
        g.append(1)
        t.append(1)
    for i in range(0, len(motifs)):
        for j in range(0, k):
            if motifs[i][j : j + 1] == 'A':
                a[j] += 1
            elif motifs[i][j : j + 1] == 'C':
                c[j] += 1
            elif motifs[i][j : j + 1] == 'G':
                g[j] += 1
            else:
                t[j] += 1
    return

def probable(pattern):
    count = 1
    for i in range(0, k):
        if pattern[i : i + 1] == 'A':
            count *= a[i]
        elif pattern[i : i + 1] == 'C':
            count *= c[i]
        elif pattern[i : i + 1] == 'G':
            count *= g[i]
        else:
            count *= t[i]
    return count

def mo():
    list = []
    for i in range(0, n):
        list.append('')
        max = 0
        tem_num = []
        for j in range(0, len(text[i]) - k + 1):
            list[i] = text[i][j : j + k]
            tem_num.append(probable(list[i]))
            if tem_num[j] > max:
                max = tem_num[j]
                tem_text = list[i]
        if max == 0:
            list[i] = text[i][0 : k]
        else:
            list[i] = tem_text
    return list

def randomized_motif_search(text, k, n):
    bestmotifs = []
    for i in range(0, n):
        ran = random.randrange(0, len(text[0]) - k + 1)
        bestmotifs.append(text[i][ran : ran + k])
    score = sc(bestmotifs)
    motifs = list(bestmotifs)
    while 0 < 1:
        pr(motifs)
        motifs = list(mo())
        if sc(motifs) < score:
            bestmotifs = list(motifs)
            score = sc(motifs)
        else:
            return bestmotifs, score

lines = sys.stdin.read().splitlines()
line1 = lines[0].split()
k = int(line1[0])
n = int(line1[1])
text = []
min = 32767
for i in range(0, n):
    text.append(lines[i + 1])
for i in range(0, 801):
    tem = randomized_motif_search(text, k, n)
    if min > tem[1]:
        min = tem[1]
        output = tem[0]
for i in range(0, len(output)):
    print(output[i])