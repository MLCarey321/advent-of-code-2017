#!/usr/bin/python3

import sys

registers = {}


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


def get_part_one(instructions):
    global registers
    last_sound = 0
    i = 0
    while True:
        command = instructions[i][0]
        args = instructions[i][1:]
        if command == 'snd':
            last_sound = get_value(args[0])
        elif command == 'set':
            set_register(args[0], args[1])
        elif command == 'add':
            set_register(args[0], get_value(args[0]) + get_value(args[1]))
        elif command == 'mul':
            set_register(args[0], get_value(args[0]) * get_value(args[1]))
        elif command == 'mod':
            set_register(args[0], get_value(args[0]) % get_value(args[1]))
        elif command == 'rcv':
            if last_sound != 0:
                set_register(args[0], last_sound)
                break
        if command == 'jgz' and get_value(args[0]) > 0:
            i += get_value(args[1])
        else:
            i += 1
        if i < 0 or i > len(instructions):
            break
    print "Part One:", last_sound


if __name__ == '__main__':
    puzzle_input = []

    while True:
        line = sys.stdin.readline()
        if len(line) > 1:
            puzzle_input.append(line.strip().split())
        else:
            break
    get_part_one(puzzle_input)
