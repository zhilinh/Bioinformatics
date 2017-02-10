import sys
sys.setrecursionlimit(2000)

def outputlcs(i, j ,level):
    global seq2_string, seq1_string
    if level == 'mid':
        if backtrack_mid[i][j] == 'upleft':
            outputlcs(i - 1, j - 1, level)
            seq1_string += seq1[i - 1]
            seq2_string += seq2[j - 1]
        elif backtrack_mid[i][j] == 'low':
            outputlcs(i, j, 'low')
        elif backtrack_mid[i][j] == 'high':
            outputlcs(i, j , 'high')
    elif level == 'low':
        if backtrack_low[i][j] == 'mid':
            outputlcs(i - 1, j, 'mid')
        elif backtrack_low[i][j] == 'up':
            outputlcs(i- 1, j, 'low')
        seq1_string += seq1[i - 1]
        seq2_string += '-'
    else:
        if backtrack_high[i][j] == 'mid':
            outputlcs(i, j - 1, 'mid')
        elif backtrack_high[i][j] == 'left':
            outputlcs(i, j - 1, 'high')
        seq1_string += '-'
        seq2_string += seq2[j - 1]
    return

blosum = {'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2}, 'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2}, 'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3}, 'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3}, 'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3}, 'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1}, 'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2}, 'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1}, 'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1}, 'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2}, 'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1}, 'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3}, 'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2}, 'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2}, 'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2}, 'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2}, 'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1}, 'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}}
lines = sys.stdin.read().splitlines()
seq1 = lines[0]
seq2 = lines[1]
s_mid = [[0]]
s_high = [[0]]
s_low = [[0]]
backtrack_mid = [['start']]
backtrack_high = [['start']]
backtrack_low = [['start']]
for i in range(len(seq1)):
    s_mid.append([-11 - i])
    s_low.append([-11 - i])
    s_high.append([float('-inf')])
    backtrack_mid.append(['low'])
    backtrack_low.append(['up'])
    backtrack_high.append(['mid'])
for j in range(len(seq2)):
    s_mid[0].append(-11 - j)
    s_high[0].append(-11 - j)
    s_low[0].append(float('-inf'))
    backtrack_mid[0].append('high')
    backtrack_high[0].append('left')
    backtrack_low[0].append('mid')

if len(seq1) < len(seq2):
    n = len(seq1)
    m = len(seq2)
else:
    n = len(seq2)
    m = len(seq1)

for d in range(n):
    for i in range(d, len(seq1)):
        s_high[i + 1].append(max(s_high[i + 1][d] - 1, s_mid[i + 1][d] - 11))
        if s_high[i + 1][-1] == s_high[i + 1][d] - 1:
            backtrack_high[i + 1].append('left')
        else:
            backtrack_high[i + 1].append('mid')
    for j in range(d, len(seq2)):
        s_low[d + 1].append(max(s_low[d][j + 1] - 1, s_mid[d][j + 1] - 11))
        if s_low[d + 1][-1] == s_low[d][j + 1] - 1:
            backtrack_low[d + 1].append('up')
        else:
            backtrack_low[d + 1].append('mid')

    s_mid[d + 1].append(max(s_high[d + 1][d + 1], s_low[d + 1][d + 1], s_mid[d][d] + blosum[seq1[d]][seq2[d]]))
    if s_mid[d + 1][-1] == s_high[d + 1][d + 1]:
        backtrack_mid[d + 1].append('high')
    elif s_mid[d + 1][-1] == s_low[d + 1][d + 1]:
        backtrack_mid[d + 1].append('low')
    else:
        backtrack_mid[d + 1].append('upleft')

    for i in range(d + 1, len(seq1)):
        s_low[i + 1].append(max(s_low[i][d + 1] - 1, s_mid[i][d + 1] - 11))
        if s_low[i + 1][-1] == s_low[i][d + 1] - 1:
            backtrack_low[i + 1].append('up')
        else:
            backtrack_low[i + 1].append('mid')

        s_mid[i + 1].append(max(s_low[i + 1][d + 1], s_high[i + 1][d + 1], s_mid[i][d] + blosum[seq1[i]][seq2[d]]))
        if s_mid[i + 1][-1] == s_high[i + 1][d + 1]:
            backtrack_mid[i + 1].append('high')
        elif s_mid[i + 1][-1] == s_low[i + 1][d + 1]:
            backtrack_mid[i + 1].append('low')
        else:
            backtrack_mid[i + 1].append('upleft')

    for j in range(d + 1, len(seq2)):
        s_high[d + 1].append(max(s_high[d + 1][j] - 1, s_mid[d + 1][j] - 11))
        if s_high[d + 1][-1] == s_high[d + 1][j] - 1:
            backtrack_high[d + 1].append('left')
        else:
            backtrack_high[d + 1].append('mid')

        s_mid[d + 1].append(max(s_low[d + 1][j + 1], s_high[d + 1][j + 1], s_mid[d][j] + blosum[seq1[d]][seq2[j]]))
        if s_mid[d + 1][-1] == s_high[d + 1][j + 1]:
            backtrack_mid[d + 1].append('high')
        elif s_mid[d + 1][-1] == s_low[d + 1][j + 1]:
            backtrack_mid[d + 1].append('low')
        else:
            backtrack_mid[d + 1].append('upleft')

#only the case, len(seq1) < len(seq2), works.
if len(seq1) != len(seq2):
    for i in range(1, n + 1):
        for j in range(n + 1, m + 1):
            s_high[i].append(max(s_high[i][j - 1] - 1, s_mid[i][j - 1] - 11))
            if s_high[i][-1] == s_high[i][j - 1] - 1:
                backtrack_high[i].append('left')
            else:
                backtrack_high[i].append('mid')
            s_low[i].append(max(s_low[i - 1][j], s_mid[i - 1][j] - 11))
            if s_low[i][-1] == s_low[i - 1][j]:
                backtrack_low[i].append('up')
            else:
                backtrack_low[i].append('mid')

            s_mid[i].append(max(s_high[i][j], s_low[i][j], s_mid[i - 1][j - 1] + blosum[seq1[i - 1]][seq2[j - 1]]))
            if s_mid[i][-1] == s_high[i][j]:
                backtrack_mid[i].append('high')
            elif s_mid[i][-1] == s_low[i][j]:
                backtrack_mid[i].append('low')
            else:
                backtrack_mid[i].append('upleft')

i = len(seq1)
j = len(seq2)
seq1_string = ''
seq2_string = ''
outputlcs(i, j, 'mid')
print(s_mid[len(seq1)][len(seq2)])
print(seq1_string)
print(seq2_string)