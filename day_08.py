#!/usr/bin/python3

import sys
import re
from copy import deepcopy

instructions = []
registers = {}
max_value = 0

while True:
    line = sys.stdin.readline()
    if len(line) > 1:
        instructions.append(line.split())
    else:
        break


def get_register_value(reg):
    global registers
    if reg not in registers.keys():
        registers[reg] = 0
    return registers[reg]


def assign_register_value(reg, value):
    global max_value, registers
    max_value = max(max_value, value)
    registers[reg] = value


for instruction in instructions:
    instruction[4] = str(get_register_value(instruction[4]))
    command = ''.join(instruction[4:7])
    triggered = eval(command)
    if eval(command):
        register = instruction[0]
        operation = instruction[1]
        diff = int(instruction[2])
        start_val = get_register_value(register)
        assign_register_value(register, start_val + diff if operation == "inc" else start_val - diff)

print "Part One:", max(registers.values())
print "Part Two:", max_value
