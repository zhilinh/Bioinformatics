import sys

spectrum = {'G':57,
'A':71,
'S':87,
'P':97,
'V':99,
'T':101,
'C':103,
'I':113,
'L':113,
'N':114,
'D':115,
'K':128,
'Q':128,
'E':129,
'M':131,
'H':137,
'F':147,
'R':156,
'Y':163,
'W':186}

def score(peptides):
    mass2 = list(mass)
    l = len(peptides)
    mass1 = [0]
    for i in range(l):
        mass1.append(peptides[i] + mass1[i])
    for i in range(1, l):
        for j in range(i, l):
            mass1.append(mass1[j + 1] - mass1[i])
    scores = 0
    for i in mass1:
        if i in mass2:
            mass2.remove(i)
            scores += 1
    return scores

def trim(leaderboard):
    linear = []
    board = {}
    step = 0
    for i in range(len(leaderboard)):
        j = score(leaderboard[i])
        linear.append(j)
        if j in board:
            board[j].append(i)
        else:
            board[j] = [i]
    linear.sort(reverse = True)
    last = 32767
    onboard = []
    for i in range(len(leaderboard)):
        if step < n:
            if linear[i] < last:
                step += len(board[linear[i]])
                last = linear[i]
                for j in board[linear[i]]:
                    onboard.append(j)
        else:
            break
    return onboard

lines = sys.stdin.read().splitlines()
peptides = lines[0].split()
n = int(lines[2])
lines[1] = lines[1].split()
mass = []
leaderboard = []
for i in lines[1]:
    mass.append(int(i))
for i in range(len(peptides)):
    leaderboard.append([])
    for j in range(len(peptides[i])):
        leaderboard[i].append(spectrum[peptides[i][j]])
output = ''
for i in trim(leaderboard):
    output += peptides[i] + ' '
print(output)