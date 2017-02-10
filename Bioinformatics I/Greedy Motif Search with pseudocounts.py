import sys

def pr(matrix):
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

def find_best_motifs(motif1):
    global a, c, g, t
    list = [motif1]
    a = []
    c = []
    g = []
    t = []
    for i in range(0, k):
        a.append(0)
        c.append(0)
        g.append(0)
        t.append(0)
        a[i] = 1
        c[i] = 1
        g[i] = 1
        t[i] = 1
        if motif1[i : i + 1] == 'A':
            a[i] += 1
        elif motif1[i : i + 1] == 'C':
            c[i] += 1
        elif motif1[i : i + 1] == 'G':
            g[i] += 1
        else:
            t[i] += 1

    for i in range(1, n):
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

        for j in range(0, k):
            a[j] = a[j] * i + 1
            c[j] = c[j] * i + 1
            g[j] = g[j] * i + 1
            t[j] = t[j] * i + 1
            if list[i][j : j + 1] == 'A':
                a[j] += 1
            elif list[i][j : j + 1] == 'C':
                c[j] += 1
            elif list[i][j : j + 1] == 'G':
                g[j] += 1
            else:
                t[j] += 1
    return list

def greedy_motif_search(text, k, n):
    bestmotifs = []
    for i in range(0, n):
        bestmotifs.append(text[i][0 : k])
    score = pr(bestmotifs)
    for i in range(0, len(text[0]) - k + 1):
        list = find_best_motifs(text[0][i : i + k])
        tem_sco = pr(list)
        if tem_sco < score:
            score = tem_sco
            bestmotifs = list
    return bestmotifs

lines = sys.stdin.read().splitlines()
line1 = lines[0].split()
k = int(line1[0])
n = int(line1[1])
text = []
for i in range(0, n):
    text.append(lines[i + 1])
output = greedy_motif_search(text, k, n)
for i in range(0, len(output)):
    print(output[i])