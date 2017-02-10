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
for i in range(len(seq1)):
    s.append([0])
    backtrack.append(['start'])
for j in range(len(seq2)):
    s[0].append(-1 * (j + 1))
    backtrack[0].append('left')
for i in range(1, len(seq1) + 1):
    for j in range(1, len(seq2) + 1):
        max_val = -float('inf')
        backtrack[i].append('')
        if s[i][j - 1] - 1 > max_val:
            max_val = s[i][j - 1] - 1
            backtrack[i][j] = 'left'
        if s[i - 1][j] - 1 > max_val:
            max_val = s[i - 1][j] - 1
            backtrack[i][j] = 'up'
        if seq1[i - 1] == seq2[j - 1]:
            same = 1
        else:
            same = -1
        if s[i - 1][j - 1] + same > max_val:
            max_val = s[i - 1][j - 1] + same
            backtrack[i][j] = 'upleft'
        s[i].append(max_val)
max_val = -float('inf')
for i in range(len(seq1) + 1):
    if s[i][len(seq2)] > max_val:
        max_val = s[i][len(seq2)]
        i_fin = i
outputlcs(backtrack, i_fin, len(seq2))
print(max_val)
print(seq1_string)
print(seq2_string)