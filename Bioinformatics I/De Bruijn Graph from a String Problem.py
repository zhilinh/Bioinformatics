import sys

lines = sys.stdin.read().splitlines()
k = int(lines[0]) - 1
text = lines[1]
node = {}
for i in range(len(text) - k):
    p = text[i : i + k]
    if not(p in node):
        node[p] = [text[i + 1 : i + 1 + k]]
    else:
        node[p].append(text[i + 1 : i + 1 + k])
for i in range(len(text) - k):
    p = text[i : i + k]
    if not(node[p] == []):
        suffix = ''
        for j in range(len(node[p])):
            suffix += node[p][j] + ','
        suffix = suffix[0 : len(suffix) - 1]
        print(p, '->', suffix)
        node[p] = []
