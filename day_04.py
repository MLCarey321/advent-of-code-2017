#!/usr/bin/python3

import sys

passphrases = []

while True:
    line = sys.stdin.readline()
    if len(line) > 1:
        passphrases.append(line)
    else:
        break

valid_count1 = 0
valid_count2 = 0

for passphrase in passphrases:
    words = passphrase.split()
    unique = set(words)
    if len(words) == len(unique):
        valid_count1 += 1
    alpha_words = map((lambda word: ''.join(sorted(word))), words)
    unique = set(alpha_words)
    if len(words) == len(unique):
        valid_count2 += 1

print "Part One:", valid_count1
print "Part Two:", valid_count2
