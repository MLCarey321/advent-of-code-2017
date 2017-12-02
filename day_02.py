#!/usr/bin/python3

import sys

rows = []
checksum1 = 0
checksum2 = 0

while True:
    line = sys.stdin.readline()
    if len(line) > 1:
        rows.append(map(int, line.split()))
    else:
        break

for row in rows:
    low = min(row)
    high = max(row)
    checksum1 += high - low
    quotient = 0
    for i in range(len(row)):
        if quotient != 0:
            checksum2 += quotient
            quotient = 0
            break
        val1 = row[i]
        for j in range(i+1, len(row)):
            val2 = row[j]
            dividend = max(val1, val2)
            divisor = min(val1, val2)
            if dividend % divisor == 0:
                quotient = dividend / divisor
                break

print "Part 1:", checksum1
print "Part 2:", checksum2
