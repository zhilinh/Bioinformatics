import sys

lines = sys.stdin.read().splitlines()
for i in lines:
    j = i.split()
    print("'" + j[0] + "':'" + j[1] + "'" + ',')
