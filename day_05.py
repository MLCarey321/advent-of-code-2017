#!/usr/bin/python3

import sys

offsets1 = []
offsets2 = []
steps1 = 0
steps2 = 0
index1 = 0
index2 = 0
part1 = False
part2 = False

while True:
    line = sys.stdin.readline()
    if len(line) > 1:
        offsets1.append(int(line))
        offsets2.append(int(line))
    else:
        break

while not part1 or not part2:
    if not part1:
        tmp = index1 + offsets1[index1]
        offsets1[index1] += 1
        index1 = tmp
        steps1 += 1
        part1 = index1 >= len(offsets1)
    if not part2:
        tmp = index2 + offsets2[index2]
        offsets2[index2] += -1 if offsets2[index2] >= 3 else 1
        index2 = tmp
        steps2 += 1
        part2 = index2 >= len(offsets2)

print "Part One:", steps1
print "Part Two:", steps2
