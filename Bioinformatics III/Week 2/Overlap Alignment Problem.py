import sys
sys.setrecursionlimit(2000)

def outputlcs(backtrack, i, j):
    global seq1_string, seq2_string
    if backtrack[i][j] == 'start':
        return
    elif backtrack[i][j] == 'upleft':
        outputlcs(backtrack, i - 1, j - 1)
        seq1_string += seq1[i - 1]
        seq2_string += seq2[j - 1]
    elif backtrack[i][j] == 'up':
        outputlcs(backtrack, i - 1, j)
        seq1_string += seq1[i - 1]
        seq2_string += '-'
    else:
        outputlcs(backtrack, i, j - 1)
        seq1_string += '-'
        seq2_string += seq2[j - 1]
    return

lines = sys.stdin.read().splitlines()
seq1 = lines[0]
seq2 = lines[1]
seq1_string = ''
seq2_string = ''
s = [[0]]
backtrack = [['start']]
max_fin = 0
i_fin = 0
j_fin = 0
for i in range(len(seq1)):
    s.append([0])
    backtrack.append(['start'])
for j in range(len(seq2)):
    s[0].append(-2 * (j + 1))
    backtrack[0].append('left')
for i in range(1, len(seq1) + 1):
    for j in range(1, len(seq2) + 1):
        max_val = -float('inf')
        backtrack[i].append('start')
        if s[i][j - 1] - 2 > max_val:
            max_val = s[i][j - 1] - 2
            backtrack[i][j] = 'left'
        if s[i - 1][j] - 2 > max_val:
            max_val = s[i - 1][j] - 2
            backtrack[i][j] = 'up'
        if seq1[i - 1] == seq2[j - 1]:
            same = 1
        else:
            same = -2
        if s[i - 1][j - 1] + same > max_val:
            max_val = s[i - 1][j - 1] + same
            backtrack[i][j] = 'upleft'
        s[i].append(max_val)
for j in range(len(seq2) + 1):
    if s[len(seq1)][j] > max_fin:
        max_fin = s[len(seq1)][j]
        j_fin = j
outputlcs(backtrack, len(seq1), j_fin)
print(max_fin)
print(seq1_string)
print(seq2_string)