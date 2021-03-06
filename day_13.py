#!/usr/bin/python3

import sys
import time


def scott_free(delay):
    global layers, sorted_depths, delay_increase
    for depth in sorted_depths:
        if (depth + delay) % (layers[depth] * 2 - 2) == 0:
            return False
        elif layers[depth] == 2:
            delay_increase = 2
    return True

layers = {}
while True:
    line = sys.stdin.readline()
    if len(line) > 1:
        sides = line.strip().split(':')
        layers[int(sides[0])] = int(sides[1].strip())
    else:
        break
start = time.time()
severity = 0
sorted_depths = [key for key, value in sorted(layers.items(), key=lambda (k, v): v)]
for layer in layers.keys():
    security_range = layers[layer]
    security = layer % (security_range * 2 - 2)
    if security == 0:
        severity += layer * security_range
print "Part One:", severity
delay_increase = 1
test_delay = 1
while not scott_free(test_delay):
    test_delay += delay_increase
print "Part Two:", test_delay
end = time.time()
print "Processing Time:", end - start
