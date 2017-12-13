#!/usr/bin/python3

import sys


def scott_free(delay):
    global layers
    for depth in layers.keys():
        if (depth + delay) % (layers[depth] * 2 - 2) == 0:
            return False
    return True

layers = {}
while True:
    line = sys.stdin.readline()
    if len(line) > 1:
        sides = line.strip().split(':')
        layers[int(sides[0])] = int(sides[1].strip())
    else:
        break
severity = 0
for layer in layers.keys():
    security_range = layers[layer]
    security = layer % (security_range * 2 - 2)
    if security == 0:
        severity += layer * security_range
print "Part One:", severity
test_delay = 1
while not scott_free(test_delay):
    test_delay += 1
print "Part Two:", test_delay
