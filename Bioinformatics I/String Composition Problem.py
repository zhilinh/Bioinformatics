import sys

lines = sys.stdin.read().splitlines()
k = int(lines[0])
text = lines[1]
for i in range(len(text) - k + 1):
    print(text[i : i + k])