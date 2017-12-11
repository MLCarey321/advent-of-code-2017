#!/usr/bin/python3

import sys

numbers = range(256)
numbers_len = len(numbers)
lengths = map(int, sys.stdin.readline().split(','))
skip_value = 0
index = 0

for length in lengths:
    if index + length >= len(numbers):
        subarray = numbers[index:numbers_len]+numbers[0:(length - (numbers_len - index))]
        rewind = list(reversed(subarray))
        numbers[index:numbers_len] = rewind[0:numbers_len-index]
        numbers[0:(length - (numbers_len - index))] = rewind[numbers_len-index:numbers_len]
    else:
        subarray = list(reversed(numbers[index:index+length]))
        numbers[index:index+length] = subarray
    index = (index + length + skip_value) % numbers_len
    skip_value += 1

print "Part One:", numbers[0] * numbers[1]
