#!/usr/bin/python3

import sys

registers = {0: {'p': 0}, 1: {'p': 1}}
active = 0


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def set_register(name, value):
    global registers, active
    registers[active][name] = get_value(value)


def get_value(value):
    global registers, active
    if is_int(value):
        return int(value)
    elif value not in registers[active].keys():
        registers[active][value] = 0
    return registers[active][value]


def inactive():
    global active
    return (active + 1) % 2


def get_part_two(instructions):
    global registers, active
    sent = {0: [], 1: []}
    i = [0, 0]
    send_count = 0
    while True:
        command = instructions[i[active]][0]
        args = instructions[i[active]][1:]
        if command == 'snd':
            sent[inactive()].append(get_value(args[0]))
            if active == 1:
                send_count += 1
        elif command == 'set':
            set_register(args[0], args[1])
        elif command == 'add':
            set_register(args[0], get_value(args[0]) + get_value(args[1]))
        elif command == 'mul':
            set_register(args[0], get_value(args[0]) * get_value(args[1]))
        elif command == 'mod':
            set_register(args[0], get_value(args[0]) % get_value(args[1]))
        elif command == 'rcv':
            if len(sent[active]) > 0:
                set_register(args[0], sent[active].pop(0))
            else:
                if len(sent[inactive()]) > 0:
                    active = inactive()
                    continue
                else:
                    break
        if command == 'jgz' and get_value(args[0]) > 0:
            i[active] += get_value(args[1])
        else:
            i[active] += 1
        if i[active] < 0 or i[active] > len(instructions):
            active = inactive()
            if i[active] < 0 or i[active] > len(instructions):
                break
    print "Part Two:", send_count


if __name__ == '__main__':
    puzzle_input = []

    while True:
        line = sys.stdin.readline()
        if len(line) > 1:
            puzzle_input.append(line.strip().split())
        else:
            break
    get_part_two(puzzle_input)
