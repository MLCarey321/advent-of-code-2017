#!/usr/bin/python3

import sys

base_weights = {}
children = {}
total_weights = {}

while True:
    line = sys.stdin.readline()
    if len(line) > 1:
        sides = line.split("->")
        lhs = sides[0].split()
        rhs = [] if len(sides) <= 1 else map(lambda node: str.strip(node), sides[1].split(","))
        base_weights[lhs[0]] = int(lhs[1].replace('(', '').replace(')', ''))
        children[lhs[0]] = rhs
    else:
        break


def find_unbalanced_program_weight(program):
    global base_weights, children, total_weights
    if len(children[program]) == 0:
        total_weights[program] = base_weights[program]
        return 0
    total_weight = base_weights[program]
    children_weights = {}
    for kid in children[program]:
        solution = find_unbalanced_program_weight(kid)
        if solution != 0:
            return solution
        child_weight = total_weights[kid]
        children_weights[kid] = child_weight
        total_weight += child_weight
    total_weights[program] = total_weight
    off_weight = min(children_weights.values(), key=lambda w: children_weights.values().count(w))
    std_weight = max(children_weights.values(), key=lambda w: children_weights.values().count(w))
    if off_weight != std_weight:
        diff = off_weight - std_weight
        for c, weight in children_weights.items():
            if weight == off_weight:
                return base_weights[c] - diff
    return 0


for parent in children.keys():
    if parent not in [child for siblings in children.values() for child in siblings]:
        print "Part One:", parent
        root_node = parent

print "Part Two:", find_unbalanced_program_weight(root_node)
