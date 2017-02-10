import sys
sys.setrecursionlimit(10000)#IMPORTANT!!!
#Applied to no divergence in nodes

def euler(start):
    global circuit, stack, ava
    suffix = lines[start][1 : k] + lines[start][k + 2 : 2 * k + 1]
    for i in info[suffix]:
        if ava[i]:
            ava[i] = False
            stack.append(i)
            euler(i)
    circuit.append(stack[-1])
    stack.pop(-1)
    return

lines = sys.stdin.read().splitlines()
k = lines[0].split()
d = int(k[1])
k = int(k[0])
lines.pop(0)
info = {}
ava = []
circuit = []
prefix_set = []
suffix_set = []
join = [0 ,0]

for i in range(len(lines)):
    prefix = lines[i][0 : k - 1] + lines[i][k + 1 : 2 * k]
    suffix = lines[i][1 : k] + lines[i][k + 2 : 2 * k + 1]
    prefix_set.append(prefix)
    suffix_set.append(suffix)
    if not prefix in info:
        info[prefix] = [i]
    else:
        info[prefix].append(i)
for i in range(len(lines)):
    prefix = lines[i][0 : k - 1] + lines[i][k + 1 : 2 * k]
    suffix = lines[i][1 : k] + lines[i][k + 2 : 2 * k + 1]
    ava.append(True)
    if not suffix in prefix_set:
        join[1] = i
    if not prefix in suffix_set:
        join[0] = i

suffix = lines[join[1]][1 : k] + lines[join[1]][k + 2 : 2 * k + 1]
info[suffix] = [join[0]]
ava[join[0]] = False
stack = [join[0]]
euler(join[0])
circuit = circuit[::-1]
prefix_string = ''
suffix_string = ''
for i in circuit:
    prefix_string += lines[i][0]
    suffix_string += lines[i][k + 1]
prefix_string += lines[circuit[-1]][1 : k]
suffix_string += lines[circuit[-1]][k + 2 : 2 * k + 1]
output = prefix_string[0 : k + d] + suffix_string
print(output)