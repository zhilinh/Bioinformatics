import sys

def ppp():
    output = ''
    max = 0
    pr = []
    for i in range(0, len(text) - k + 1):
        pattern = text[i : i + k]
        count = 1
        for j in range(0, k):
            if pattern[j : j + 1] == 'A':
                count *= a[j]
            elif pattern[j : j + 1] == 'C':
                count *= c[j]
            elif pattern[j : j + 1] == 'G':
                count *= g[j]
            else:
                count *= t[j]
        pr.append(count)
        if count > max:
            max = count
    for i in range(0, len(text) - k + 1):
        if pr[i] == max:
            output = text[i : i + k]
            return output

lines = sys.stdin.read().splitlines()
text = lines[0]
k = int(lines[1])
a = lines[2].split()
c = lines[3].split()
g = lines[4].split()
t = lines[5].split()
a = [float(a) for a in a if a]  #string lists converted into int lists
c = [float(c) for c in c if c]
g = [float(g) for g in g if g]
t = [float(t) for t in t if t]

print(ppp())

