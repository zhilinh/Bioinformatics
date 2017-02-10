import sys

lines = sys.stdin.read().splitlines()
info = {}
id = {}
od = {}
node = []
for i in range(len(lines)):
    prefix = lines[i][0 : len(lines[i]) - 1]
    suffix = lines[i][1 : len(lines[i])]
    if not prefix in node:
        node.append(prefix)
    if not prefix in info:
        info[prefix] = [suffix]
        od[prefix] = 1
    else:
        info[prefix].append(suffix)
        od[prefix] += 1
for i in node:
    for j in info[i]:
        if not j in id:
            id[j] = 1
        else:
            id[j] += 1
        if not j in node:
            od[j] = 0
for i in node:
    if not i in id:
        id[i] = 0

path = []
for i in node:
    if not(id[i] == 1 and od[i] == 1):
        if od[i] > 0:
            for j in info[i]:
                tem_path = [i, j]
                k = j
                while id[k] == 1 and od[k] == 1:
                    tem_path.append(info[k][0])
                    k = info[k][0]
                path.append(tem_path)
for i in path:
    k = i[0]
    for j in range(1, len(i)):
        k += i[j][-1]
    print(k)