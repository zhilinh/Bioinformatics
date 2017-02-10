def mismatch(p, g, d):
    output = 0
    for i in range(0, len(g) - len(p) + 1):
        t = g[i : i + len(p)]
        count = 0
        for j in range(0, len(p)):
            if count > d:
                break
            else:
                if t[j : j + 1] != p[j : j + 1]:
                    count += 1
        if count <= d:
            output += 1
    return output

def hd(a, b):
    count = 0
    for i in range(0, len(a)):
        if a[i:i+1] != b[i:i+1]:
            count += 1
    return count

def neighbors(p, d):
    if d == 0:
        return [p]
    if len(p) == 1:
        return ['A', 'C', 'G', 'T']
    n = []
    sn = neighbors(p[1:], d)
    for i in range(0, len(sn)):
        if hd(p[1:], sn[i]) < d:
            n.append('A'+sn[i])
            n.append('C'+sn[i])
            n.append('G'+sn[i])
            n.append('T'+sn[i])
        else:
            n.append(p[0 : 1]+sn[i])
    return n

def matchpattern(p, line):
    for i in range(0, number):
        if line != i:
            count = 0
            for j in range(0, len(pattern[i])):
                if pattern[i][j] == p:
                    count = 1
                    break
            if count == 0:
                return False
    return True

k = int(input('k'))
d = int(input('d'))
number = int(input('number'))
g = []
pattern = []
output = []
for i in range(0, number):
    g.append(input('g'))
    pattern.append([])
array = {}

for i in range(0, number):
    for j in range(0, len(g[i]) - k + 1):
        pattern[i].extend(neighbors(g[i][j : j + k], d))
        
for i in range(0, number):
    for j in range(0, len(pattern[i])):
        if not(array.has_key(pattern[i][j])):
            if matchpattern(pattern[i][j], i):
                array[pattern[i][j]] = 1
                output.append(pattern[i][j])
            else:
                array[pattern[i][j]] = 0
out = ''
for i in range(0, len(output)):
    out += output[i] + ' '
print(out)