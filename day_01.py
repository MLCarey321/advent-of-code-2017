#!/usr/bin/python3

digits = str(input("? "))
matches1 = 0
matches2 = 0

for i in range(len(digits)):
    if digits[i] == digits[(i+1) % len(digits)]:
        matches1 += int(digits[i])
    if digits[i] == digits[(i+(len(digits)/2)) % len(digits)]:
        matches2 += int(digits[i])

print matches1
print matches2
