#!/usr/bin/python3

puzzle = str(input("? "))

banks = map(int, puzzle.split())
combos = [''.join(puzzle)]
magic_combo = ""


def get_cycle_count(f):
    cycles = 0
    while True:
        cycles += 1
        max_blocks = max(banks)
        index = banks.index(max_blocks)
        divvy = max(max_blocks / len(banks), 1)
        banks[index] = 0
        redistributed = 0
        while redistributed < max_blocks:
            index = (index + 1) % len(banks)
            banks[index] += divvy
            redistributed += divvy
            if divvy > (max_blocks - redistributed):
                divvy = 1
        combo = ''.join(map(str, banks))
        if f(combo):
            break
        combos.append(combo)
    return cycles


print "Part One", get_cycle_count((lambda c: c in combos))
magic_combo = ''.join(map(str, banks))
print "Part Two", get_cycle_count((lambda c: c == magic_combo))
