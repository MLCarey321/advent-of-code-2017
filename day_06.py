#!/usr/bin/python3

puzzle = str(input("? "))

blocks = map(int, puzzle.split())
combos = [''.join(puzzle)]
magic_combo = ""


def get_attempt_count(f):
    attempts = 0
    while True:
        attempts += 1
        amount = max(blocks)
        index = blocks.index(amount)
        divvy = max(amount / len(blocks), 1)
        blocks[index] = 0
        given = 0
        while given < amount:
            index = (index + 1) % len(blocks)
            blocks[index] += divvy
            given += divvy
            if divvy > (amount - given):
                divvy = 1
        combo = ''.join(map(str, blocks))
        if f(combo):
            break
        combos.append(combo)
    return attempts


print "Part One", get_attempt_count((lambda c: c in combos))
magic_combo = ''.join(map(str, blocks))
print "Part Two", get_attempt_count((lambda c: c == magic_combo))
