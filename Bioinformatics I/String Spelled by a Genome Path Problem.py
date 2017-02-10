import sys

lines = sys.stdin.read().splitlines()
output = lines[0]
for i in range(1, len(lines)):
    output += lines[i][-1]
print(output)
