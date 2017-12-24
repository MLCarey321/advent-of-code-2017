#!/usr/bin/python3

import time

step_size = input("? ")
circular_buffer = [0]
index = 0
false_code = 0
kill_code = 0

start = time.time()

for i in range(2017):
    index = ((index + step_size) % len(circular_buffer)) + 1
    circular_buffer.insert(index, i+1)

false_code = circular_buffer[index + 1]

for i in range(50000000):
    index = ((index + step_size) % (i + 1)) + 1
    if index == 1:
        kill_code = i+1

end = time.time()

print "Part One:", false_code
print "Part Two:", kill_code
print "Processing Time:", end - start
