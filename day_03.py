#!/usr/bin/python3

value = input("? ")
grid = {(0, 0): 1}


def get_value_for_coordinates(x, y):
    global grid
    total = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            total += 0 if (x + dx, y + dy) not in grid.keys() else grid[(x + dx, y + dy)]
    grid[(x, y)] = total
    return total


def get_highest_for_side(base, fx, fy):
    global value
    side_highest = 0
    square_size = (level * 2) + 1
    for delta in range(1, square_size):
        side_highest = get_value_for_coordinates(fx(base, delta), fy(base, delta))
        if side_highest > value:
            break
    return side_highest


i = 1
counter = 0
while i * i < value:
    i += 2
    counter += 1
print "Part One:", counter * 2 - (i ** 2 - value)

highest = 0
level = 0
while True:
    level += 1
    highest = get_highest_for_side(level, (lambda l, d: l), (lambda l, d: -l + d))
    if highest > value:
        break
    highest = get_highest_for_side(level, (lambda l, d: l - d), (lambda l, d: l))
    if highest > value:
        break
    highest = get_highest_for_side(level, (lambda l, d: -l), (lambda l, d: l - d))
    if highest > value:
        break
    highest = get_highest_for_side(level, (lambda l, d: -l + d), (lambda l, d: -l))
    if highest > value:
        break
print "Part Two:", highest
