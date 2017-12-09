#!/usr/bin/python3

import sys

stream = sys.stdin.readline()
stream_total = 0
group_value = 1
in_garbage = False
ignore_next = False
garbage_count = 0

for char in stream:
    if not in_garbage:
        if char == '{':
            stream_total += group_value
            group_value += 1
        elif char == '}':
            group_value -= 1
        elif char == '<':
            in_garbage = True
    elif ignore_next:
        ignore_next = False
    elif char == '!':
        ignore_next = True
    elif char == '>':
        in_garbage = False
    else:
        garbage_count += 1

print "Part One:", stream_total
print "Part Two:", garbage_count
