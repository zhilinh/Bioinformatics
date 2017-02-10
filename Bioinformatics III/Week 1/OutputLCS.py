import sys
sys.setrecursionlimit(2000)

def outputlcs(backtrack, v, i, j):
    global output
    if i == 0 or j == 0:
        return
    if backtrack[i][j] == 1:
        outputlcs(backtrack, v, i - 1, j - 1)
        output.append(v[j - 1])
    elif backtrack[i][j] == 2:
        outputlcs(backtrack, v, i - 1, j)
    else:
        outputlcs(backtrack, v, i, j - 1)
    return

lines = sys.stdin.read().splitlines()
s = [[0]]
backtrack = [[0]]
output = []
output_string = ''
for i in range(len(lines[0])):
    s[0].append(0)
    backtrack[0].append(0)
for j in range(len(lines[1])):
    s.append([0])
    backtrack.append([0])
for i in range(1, len(lines[1]) + 1):
    for j in range(1, len(lines[0]) + 1):
        same = 0
        if lines[0][j - 1] == lines[1][i - 1]:
            same = s[i - 1][j - 1] + 1
        s[i].append(max(s[i - 1][j], s[i][j - 1], same))
        if s[i][j] == same:
            backtrack[i].append(1)
        elif s[i][j] == s[i - 1][j]:
            backtrack[i].append(2)
        else:
            backtrack[i].append(3)
outputlcs(backtrack, lines[0], i, j)
for i in output:
    output_string += str(i)
print(output_string)

#while i > 0 and j > 0:
#   if backtrack[i,j] = 1:
#       LCS.append(v[i-1])
#       i <- i-1
#       j <- j-1
#   else if backtrack[i,j] = 2:
#           i <- i-1
#        else:
#           j <- j-1
# return reversed(LCS)