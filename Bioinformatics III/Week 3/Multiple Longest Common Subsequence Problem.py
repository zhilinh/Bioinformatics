import sys

lines = sys.stdin.read().splitlines()
seq1 = lines[0]
seq2 = lines[1]
seq3 = lines[2]
s = {}
backtrack = {(0, 0, 0) : 0}
for i in range(len(seq1) + 1):
    for j in range(len(seq2) + 1):
        s[(i, j, 0)] = 0
        backtrack[(i, j, 0)] = 2
for i in range(len(seq1) + 1):
    for k in range(len(seq3) + 1):
        s[(i, 0, k)] = 0
        backtrack[(i, 0, k)] = 1
for j in range(len(seq2) + 1):
    for k in range(len(seq3) + 1):
        s[(0, j, k)] = 0
        backtrack[(0, j, k)] = 3
backtrack[(0, 0, 0)] = 0

for i in range(1, len(seq1) + 1):
    for j in range(1, len(seq2) + 1):
        for k in range(1, len(seq3) + 1):
            if seq1[i - 1] == seq2[j - 1] and seq2[j - 1] == seq3[k - 1]:
                max_val = s[i - 1, j - 1, k - 1] + 1
            else:
                max_val = 0
            s[(i, j , k)] = max(s[(i - 1, j, k)], s[(i, j - 1, k)], s[(i, j , k - 1)], s[(i - 1, j - 1, k)], s[(i - 1, j, k - 1)], s[(i, j - 1, k - 1)], max_val)
            if s[(i, j, k)] == s[(i - 1, j, k)]:
                backtrack[(i, j, k)] = 1
            elif s[(i, j, k)] == s[(i, j - 1, k)]:
                backtrack[(i, j, k)] = 2
            elif s[(i, j, k)] == s[(i, j, k - 1)]:
                backtrack[(i, j , k)] = 3
            elif s[(i, j, k)] == s[(i - 1, j - 1, k)]:
                backtrack[(i, j, k)] = 4
            elif s[(i, j, k)] == s[(i - 1, j, k - 1)]:
                backtrack[(i, j, k)] = 5
            elif s[(i, j, k)] == s[(i, j - 1, k - 1)]:
                backtrack[(i, j, k)] = 6
            else:
                backtrack[(i, j, k)] = 7

seq1_string = ''
seq2_string = ''
seq3_string = ''
print(s[(i, j, k)])
while i > 0 or j > 0 or k > 0:
    if backtrack[(i, j, k)] == 1:
        i -= 1
        seq1_string += seq1[i]
        seq2_string += '-'
        seq3_string += '-'
    elif backtrack[(i, j, k)] == 2:
        j -= 1
        seq1_string += '-'
        seq2_string += seq2[j]
        seq3_string += '-'
    elif backtrack[(i, j, k)] == 3:
        k -= 1
        seq1_string += '-'
        seq2_string += '-'
        seq3_string += seq3[k]
    elif backtrack[(i, j, k)] == 4:
        i -= 1
        j -= 1
        seq1_string += seq1[i]
        seq2_string += seq2[j]
        seq3_string += '-'
    elif backtrack[(i, j, k)] == 5:
        i -= 1
        k -= 1
        seq1_string += seq1[i]
        seq2_string += '-'
        seq3_string += seq3[k]
    elif backtrack[(i, j, k)] == 6:
        j -= 1
        k -= 1
        seq1_string += '-'
        seq2_string += seq2[j]
        seq3_string += seq3[k]
    else:
        i -= 1
        j -= 1
        k -= 1
        seq1_string += seq1[i]
        seq2_string += seq2[j]
        seq3_string += seq3[k]
print(seq1_string[::-1])
print(seq2_string[::-1])
print(seq3_string[::-1])