#!/usr/bin/python3

import sys


def get_distance_from_start(x, y):
    abs_x = abs(x)
    abs_y = abs(y)
    distance = min(abs_x, abs_y)
    abs_x -= distance
    abs_y -= distance
    distance += (abs_y / 2) + abs_x
    return distance

child_path = sys.stdin.readline().strip().split(',')
child_x = 0
child_y = 0
longest_distance = 0
for step in child_path:
    if 'n' in step:
        child_y += 2 / len(step)
    elif 's' in step:
        child_y -= 2 / len(step)
    if 'e' in step:
        child_x += 1
    elif 'w' in step:
        child_x -= 1
    longest_distance = max(longest_distance, get_distance_from_start(child_x, child_y))
shortest_distance = get_distance_from_start(child_x, child_y)
print "Part One:", shortest_distance
print "Part Two:", longest_distance
