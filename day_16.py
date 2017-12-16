#!/usr/bin/python3

import sys


def swap_indexes(i1, i2):
    global programs
    tmp = programs[i1]
    programs[i1] = programs[i2]
    programs[i2] = tmp

print "?"
instructions = sys.stdin.readline().strip().split(",")
iterations = {0: 'abcdefghijklmnop'}
programs = list(iterations[0])
for i in range(1, 1000):
    for instruction in instructions:
        if instruction[0] == 's':
            spin_amount = int(instruction[1:]) % len(programs)
            programs = programs[len(programs)-spin_amount:] + programs[0:len(programs)-spin_amount]
        elif instruction[0] == 'x':
            positions = instruction[1:].split('/')
            swap_indexes(int(positions[0]), int(positions[1]))
        elif instruction[0] == 'p':
            partners = instruction[1:].split('/')
            index_1 = programs.index(partners[0])
            index_2 = programs.index(partners[1])
            swap_indexes(index_1, index_2)
    if ''.join(programs) == iterations[0]:
        break
    else:
        iterations[i] = ''.join(programs)
print "Part One:", iterations[1]
print "Part Two:", iterations[1000000000 % i]
