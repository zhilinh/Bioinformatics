import sys
def pmp(p, g):
    output = ''
    for i in range(0, len(g)):
        if p == g[i : i + len(p)]:
            output += str(i) + ' '    
    return output

lines = sys.stdin.read().splitlines()
p = lines[0]
g = lines[1]
print(pmp(p, g))
