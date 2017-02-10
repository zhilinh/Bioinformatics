import sys

def outputlcs(source, next):
    global output, backtrack
    if next == source:
        return
    outputlcs(source, backtrack[next])
    output.append(backtrack[next])
    return

def longestpath(source, next, sink):
    global outnode, innode, edge, ava, backtrack
    if ava[source] + edge[source, next] >= ava[next]:
        ava[next] = ava[source] + edge[source, next]
        if not next in outnode:
            backtrack[next] = source
            return
        if source == sink:
            return
        for i in outnode[next]:
            longestpath(next, i, sink)
        backtrack[next] = source
    return

lines = sys.stdin.read().splitlines()
source = int(lines[0])
sink = int(lines[1])
output = []
output_string = ''
ava = {}
edge = {}
innode = {}
outnode = {}
backtrack = {}
node = []
for i in range(2, len(lines)):
    lines[i] = lines[i].split('->')
    lines[i][0] = int(lines[i][0])
    lines[i][1] = lines[i][1].split(':')
    lines[i].append(int(lines[i][1][1]))
    lines[i][1] = int(lines[i][1][0])
    if lines[i][0] in outnode:
        outnode[lines[i][0]].append(lines[i][1])
    else:
        outnode[lines[i][0]] = [lines[i][1]]
    if lines[i][1] in innode:
        innode[lines[i][1]].append(lines[i][0])
    else:
        innode[lines[i][1]] = [lines[i][0]]
    edge[(lines[i][0], lines[i][1])] = lines[i][2]
    if not lines[i][0] in node:
        node.append(lines[i][0])
        ava[lines[i][0]] = 0
    if not lines[i][1] in node:
        node.append(lines[i][1])
        ava[lines[i][1]] = 0

for i in node:
    if not i in innode and i != source:
        for j in outnode[i]:
            innode[j].remove(i)
            edge.pop((i, j))
        outnode.pop(i)
for i in outnode[source]:
    longestpath(source, i, sink)
print(ava[sink])
outputlcs(source, sink)
output.append(sink)
for i in output:
    output_string += str(i) + '->'
print(output_string[:-2])