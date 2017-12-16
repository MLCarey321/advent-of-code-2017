#!/usr/bin/python3

gen_a_value = input("Generator A? ")
gen_b_value = input("Generator B? ")
gen_matches = []
match_count = 0

for i in range(40000000):
    gen_a_value = gen_a_value * 16807 % 2147483647
    gen_b_value = gen_b_value * 48271 % 2147483647
    gen_a_binary = bin(gen_a_value)[2:].zfill(32)[16:]
    gen_b_binary = bin(gen_b_value)[2:].zfill(32)[16:]
    if gen_a_binary == gen_b_binary:
        match_count += 1

print "Part One:", match_count
