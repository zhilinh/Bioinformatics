import sys

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
            for j in new_table:
                k = list(i)
                k.append(j)
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

table = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
new_table = []
score_set = {}
lines = sys.stdin.read().splitlines()
lines[1] = lines[1].split()
n = int(lines[0])
mass = []
leaderboard = []
for i in lines[1]:
    mass.append(int(i))
for i in table:
    if i in mass:
        new_table.append(i)
        leaderboard.append([i])
        score_set[tuple([i])] = 2
output = ''
for i in expand(leaderboard):
    output += str(i) + '-'
output = output[0 : len(output) - 1]
print(output)