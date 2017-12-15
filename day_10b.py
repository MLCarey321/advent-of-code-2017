#!/usr/bin/python3

import sys
import numpy


def get_knot_hash(string):
    lengths = map(ord, string.strip())
    numbers = range(256)
    numbers_len = len(numbers)
    lengths += [17, 31, 73, 47, 23]
    skip_value = 0
    index = 0

    for i in range(64):
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

    dense_bits = []
    for sparse_range in range(16):
        dense_bits.append(numpy.bitwise_xor.reduce(numbers[sparse_range*16:sparse_range*16+16]))

    return ''.join(map((lambda bits: str(format(bits, '#04x'))[2:]), dense_bits))

if __name__ == '__main__':
    print get_knot_hash(sys.stdin.readline())
