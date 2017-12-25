#!/usr/bin/python3

import sys
from day_22a import get_part_one
from day_22b import get_part_two

puzzle_input = []

while True:
    line = sys.stdin.readline()
    if len(line) > 1:
        puzzle_input.append(line.strip())
    else:
        break
get_part_one(puzzle_input)
get_part_two(puzzle_input)
