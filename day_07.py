#!/usr/bin/python3

import sys

lhs = []
rhs = []
tree = []
are_children = []
has_children = []
weights = {}
children = {}
total_weights = {}


def get_total_weight(program):
    if program in total_weights.keys():
        return total_weights[program]
    weight = weights[program]
    for child in children[program]:
        weight += get_total_weight(child)
    total_weights[program] = weight
    return weight


def find_unbalanced_program_weight(program):
    if len(children[program]) == 0:
        return
    solution = 0
    children_weights = {}
    for child in children[program]:
        children_weights[child] = get_total_weight(child)
        solution = max(solution, find_unbalanced_program_weight(child))
    if solution > 0:
        return solution
    unique_weights = set(children_weights.values())
    if len(unique_weights) > 1:
        weight_count = {}
        for weight in unique_weights:
            weight_count[weight] = 0
        for weight in children_weights.values():
            weight_count[weight] += 1
        off_weight = min(weight_count, key=weight_count.get)
        std_weight = max(weight_count, key=weight_count.get)
        diff = off_weight - std_weight
        for child, weight in children_weights.items():
            if weight == off_weight:
                return weights[child] - diff


while True:
    line = sys.stdin.readline()
    if len(line) > 1:
        sides = line.split("->")
        lhs = sides[0].split()
        if len(sides) > 1:
            rhs = map(lambda node: str.strip(node), sides[1].split(","))
            has_children.append(lhs[0])
            are_children += rhs
        else:
            rhs = []
        weights[lhs[0]] = int(lhs[1].replace('(','').replace(')',''))
        children[lhs[0]] = rhs
    else:
        break

root_node = ""
for parent in has_children:
    if parent not in are_children:
        print "Part One:", parent
        root_node = parent
        break

get_total_weight(root_node)
print "Part Two:", find_unbalanced_program_weight(root_node)
