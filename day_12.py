#!/usr/bin/python3

import sys


def get_group_for_program(program_id, seen):
    group = programs[program_id]
    seen.add(program_id)
    addendum = set()
    for group_member in group:
        if group_member not in seen:
            addendum.update(get_group_for_program(group_member, seen))
            seen.update(addendum)
    group.update(addendum)
    return group

programs = {}
while True:
    line = sys.stdin.readline().strip()
    if len(line) > 1:
        sides = line.split(' <-> ')
        programs[int(sides[0])] = set(map((lambda pgm: int(pgm.strip())), sides[1].split(',')))
    else:
        break
grouped = get_group_for_program(0, set())
print "Part One:", len(grouped)
group_count = 1
while len(grouped) < len(programs.keys()):
    program = [ungrouped for ungrouped in programs.keys() if ungrouped not in grouped][0]
    grouped.update(get_group_for_program(program, set()))
    group_count += 1
print "Part Two:", group_count
