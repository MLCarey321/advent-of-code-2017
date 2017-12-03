#!/usr/bin/python3

square = input("? ")

i = 1
counter = 0

length = 15
grid = [[0 for x in range(length)] for y in range(length)]
x = length / 2
y = length / 2
depth = 0
grid[x][y] = 1
x += 1
total = 0


def get_total(x, y):
    ret_val = 0
    ret_val += grid[y-1][x]
    ret_val += grid[y-1][x-1]
    ret_val += grid[y-1][x+1]
    ret_val += grid[y+1][x]
    ret_val += grid[y+1][x-1]
    ret_val += grid[y+1][x+1]
    ret_val += grid[y][x-1]
    ret_val += grid[y][x+1]
    return ret_val

while True:
    if i*i >= square:
        break
    else:
        i += 2
        counter += 1

distance = counter * 2 - (i**2 - square)
print "Part One:", distance

while True:
    depth += 1
    for delta in range((depth*2)-1):
        total = get_total(x, y)
        grid[y][x] = total
        y -= 1
        if total > square:
            break
    if total > square:
        break

    for delta in range((depth*2)):
        total = get_total(x, y)
        grid[y][x] = total
        x -= 1
        if total > square:
            break
    if total > square:
        break

    for delta in range((depth*2)):
        total = get_total(x, y)
        grid[y][x] = total
        y += 1
        if total > square:
            break
    if total > square:
        break

    for delta in range((depth*2)+1):
        total = get_total(x, y)
        grid[y][x] = total
        x += 1
        if total > square:
            break
    if total > square:
        break

print "Part Two:", total
print_length = "%"+str(len(str(total)))+"s"
for row in range(length):
    print "\t".join(map((lambda nbr: print_length % nbr), grid[row]))
