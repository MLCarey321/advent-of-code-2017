#!/usr/bin/python3

import sys
from copy import deepcopy


def add_rotations(old_input, output):
    global rules
    for rotation in range(3):
        new_input = map(lambda x: list(x), deepcopy(old_input))
        size = len(new_input)
        for r in range(size):
            for c in range(size):
                new_input[r][c] = old_input[size - c - 1][r]
        new_input = tuple(map(lambda x: tuple(x), new_input))
        rules[new_input] = output
        old_input = new_input


def add_flips(old_input, output):
    global rules
    new_input = map(lambda x: list(x), deepcopy(old_input))
    size = len(new_input)
    for r in range(size):
        for c in range(size):
            new_input[r][c] = old_input[r][size-c-1]
    new_input = tuple(map(lambda x: tuple(x), new_input))
    rules[new_input] = output
    new_input = map(lambda x: list(x), deepcopy(old_input))
    for r in range(size):
        for c in range(size):
            new_input[r][c] = old_input[size-r-1][c]
    new_input = tuple(map(lambda x: tuple(x), new_input))
    rules[new_input] = output

rules = {}
while True:
    line = sys.stdin.readline()
    if len(line) > 1:
        lhs, rhs = line.split('=>')
        rules[tuple(map(lambda x: tuple(x), lhs.strip().split('/')))] = tuple(map(lambda x: tuple(x), rhs.strip().split('/')))
    else:
        break

new_rule_count = len(rules)
rule_count = 0
while new_rule_count > rule_count:
    rule_count = new_rule_count
    for lhs, rhs in deepcopy(rules).iteritems():
        add_flips(lhs, rhs)
        add_rotations(lhs, rhs)
    new_rule_count = len(rules)

pattern = [list('.#.'), list('..#'), list('###')]
for iteration in range(1, 19):
    grid_size = len(pattern)
    new_pattern = []
    step = 2 if grid_size % 2 == 0 else 3
    for row in range(0, grid_size, step):
        new_row = []
        for col in range(0, grid_size, step):
            sub_pattern = []
            for sub_row in range(step):
                sub_pattern.append(tuple(pattern[row + sub_row][col:col+step]))
            sub_pattern = tuple(sub_pattern)
            if col == 0:
                new_row += rules[sub_pattern]
            else:
                addition = rules[sub_pattern]
                for i in range(len(new_row)):
                    new_row[i] += addition[i]
        new_pattern += new_row
    print iteration, ''.join(map(lambda x: ''.join(list(x)), new_pattern)).count('#')
    pattern = new_pattern
