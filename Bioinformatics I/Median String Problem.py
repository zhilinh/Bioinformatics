import sys
def numbertopattern(i, k):
    mod = []
    x = 0
    while i > 0:
        m = i % 4
        mod.append('A')
        if m == 3:
            mod[x] = 'T'
        elif m == 2:
            mod[x] = 'G'
        elif m == 1:
            mod[x] = 'C'
        i = i // 4
        x += 1
    for i in range(x, k):
        mod.append('A')
    out = ''
    while k > 0:
        k -= 1
        out += mod[k]
    return out

def hd(a, b):
    count = 0
    for i in range(0, len(a)):
        if a[i:i+1] != b[i:i+1]:
            count += 1
    return count

def dbpas(p, g):
    k = len(p)
    l = len(g[0])
    distance = 0
    for i in range(0, n):
        hamming = 32765
        for j in range(0, l - k + 1):
            m = hd(p, g[i][j : j + k])
            if hamming > m:
                hamming = m
        distance += hamming
    return distance

def medianstring(g, k):
    distance = 32765
    median = ''
    for i in range(0, 4 ** k - 1):
        pattern = numbertopattern(i, k)
        x = dbpas(pattern, g)
        if distance > x:
            distance = x
            median = pattern
    return median

lines = sys.stdin.read().splitlines()
k = int(lines[0])
n = len(lines) - 1
g = []
for i in range(1, n + 1):
    g.append(lines[i])
print(medianstring(g, k))
