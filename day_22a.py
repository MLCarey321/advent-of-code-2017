#!/usr/bin/python3

import sys
from collections import defaultdict


def get_part_one(nodes):
    grid = defaultdict(lambda: '.')
    num_rows = len(nodes)
    num_cols = len(nodes[0])
    for row in range(num_rows):
        for col in range(num_cols):
            grid[col, row] = nodes[row][col]
    x = num_cols / 2
    y = num_rows / 2
    dx = 0
    dy = -1
    infect_bursts = 0
    for i in range(10000):
        if grid[x, y] == '.':
            tmp = dx
            dx = dy
            dy = -tmp
            grid[x, y] = '#'
            infect_bursts += 1
        else:
            tmp = dx
            dx = -dy
            dy = tmp
            grid[x, y] = '.'
        x += dx
        y += dy
    print "Part One:", infect_bursts

if __name__ == '__main__':
    puzzle_input = []

    while True:
        line = sys.stdin.readline()
        if len(line) > 1:
            puzzle_input.append(line.strip())
        else:
            break
    get_part_one(puzzle_input)
