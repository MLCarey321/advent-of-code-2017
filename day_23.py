#!/usr/bin/python3

import sys


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def set_register(name, value):
    global registers
    registers[name] = get_value(value)


def get_value(value):
    global registers
    if is_int(value):
        return int(value)
    elif value not in registers.keys():
        registers[value] = 0
    return registers[value]


registers = {}
instructions = []
while True:
    line = sys.stdin.readline()
    if len(line) > 1:
        instructions.append(line.strip().split())
    else:
        break
i = 0
mul_count = 0
while True:
    command = instructions[i][0]
    args = instructions[i][1:]
    if command == 'set':
        set_register(args[0], args[1])
    elif command == 'sub':
        set_register(args[0], get_value(args[0]) - get_value(args[1]))
    elif command == 'mul':
        set_register(args[0], get_value(args[0]) * get_value(args[1]))
        mul_count += 1
    if command == 'jnz' and get_value(args[0]) != 0:
        i += get_value(args[1])
    else:
        i += 1
    if i < 0 or i >= len(instructions):
        break
print "Part One:", mul_count
h = 0
for i in range(109900, 126901, 17):
    for g in range(2, i):
        if i % g == 0:
            h += 1
            break
print "Part Two:", h
