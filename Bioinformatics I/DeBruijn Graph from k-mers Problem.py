import sys

lines = sys.stdin.read().splitlines()
node = {}
output= {}
for p in lines:
    node[p] = [p[0 : len(p) - 1], p[1 : len(p)]]
    if not(node[p][0] in output):
        output[node[p][0]] = [node[p][1]]
    else:
        output[node[p][0]].append(node[p][1])
for p in lines:
    if output[node[p][0]] != []:
        suffix = ''
        for i in range(len(output[node[p][0]])):
            suffix += output[node[p][0]][i] + ','
        suffix = suffix[0 : len(suffix) - 1]
        print(node[p][0], '->', suffix)
        output[node[p][0]] = []