import sys
#Max(N) ?= 8 or 9

def score(peptides):
    global score_set
    plus = peptides[-1]
    sum_mass = plus
    peptides.pop(-1)
    if plus in mass:
        scores = score_set[tuple(peptides)] + 1
    else:
        scores = score_set[tuple(peptides)]
    for i in range(1, len(peptides) + 1):
        sum_mass += peptides[-i]
        if sum_mass in mass:
            scores += 1
    peptides.append(plus)
    score_set[tuple(peptides)] = scores
    return scores

def top(mass):
    count = {}
    for i in range(1, len(mass)):
        for j in range(i):
            k = mass[i] - mass[j]
            if k != 0:
                if k in count:
                    count[k] += 1
                else:
                    count[k] = 1
    result = sorted(count.items(), key = lambda d : d[1], reverse = True)
    output = []
    step = 0
    max = 32767
    for i in result:
        if step < n and 56 < i[0] < 201:
            if i[1] < max:
                max = i[1]
                output.append(i[0])
                step += 1
            elif i[1] == max:
                output.append(i[0])
    return output

def trim(leaderboard):
    count = {}
    for i in leaderboard:
        j = score_set[tuple(i)]
        count[tuple(i)] = j
    result = sorted(count.items(), key = lambda d : d[1], reverse = True)
    output = []
    step = 0
    max = 32767
    for i in result:
        if step < n:
            if i[1] < max:
                max = i[1]
                output.append(list(i[0]))
                step += 1
            elif i[1] == max:
                output.append(list(i[0]))
        else:
            break
    return output

def expand(leaderboard):
    max = 0
    while leaderboard != []:
        newboard = []
        for i in leaderboard:
            for j in table:
                k = list(i)
                k.append(j)
                if not tuple(k) in score_set:
                    score_set[tuple(k)] = score(k)
                newboard.append(k)
        leaderboard_copy = list(newboard)
        for i in range(len(leaderboard_copy)):
            summary = sum(leaderboard_copy[i])
            if summary == mass[-1]:
                if score(leaderboard_copy[i]) > max:
                    max = score(leaderboard_copy[i])
                    final = leaderboard_copy[i]
            elif summary > mass[-1] - 57:
                newboard.remove(leaderboard_copy[i])
        if len(newboard) > n:
            leaderboard = trim(newboard)
        else:
            leaderboard = list(newboard)
    return final

lines = sys.stdin.read().splitlines()
old_table = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
m = int(lines[0])
n = int(lines[1])
score_set = {}
leaderboard = []
mass = lines[2].split()
for i in range(len(mass)):
    mass[i] = int(mass[i])
mass.append(0)
mass.sort()
table = top(mass)
for i in table:
    score_set[tuple([i])] = 2
    leaderboard.append([i])
output = ''
for i in expand(leaderboard):
    output += str(i) + '-'
output = output[0 : len(output) - 1]
print(output)