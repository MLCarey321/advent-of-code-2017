#!/usr/bin/python3

import sys
import day_10b


def free_block(x, y):
    global hashes
    if x in range(128) and y in range(128) and hashes[x][y] == '1':
        hashes[x][y] = '0'
        free_block(x-1, y)
        free_block(x+1, y)
        free_block(x, y-1)
        free_block(x, y+1)

key = sys.stdin.readline().strip()
hashes = []
for suffix in range(128):
    knot_hash = day_10b.get_knot_hash(key + '-' + str(suffix))
    hashes.append(list(bin(int(knot_hash, 16))[2:].zfill(128)))
used_count = 0
for row in hashes:
    used_count += row.count('1')
print "Part One:", used_count
block_count = 0
for row in range(128):
    for col in range(128):
        if hashes[row][col] == '1':
            block_count += 1
            free_block(row, col)
print "Part Two:", block_count
