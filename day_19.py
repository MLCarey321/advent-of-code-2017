#!/usr/bin/python3

import sys

maze = []
while True:
    line = sys.stdin.readline()
    if len(line) > 1:
        maze.append(list(line))
    else:
        break
y = 0
x = maze[0].index('|')
x_diff = 0
y_diff = 1
seen = []
steps = 1
while True:
    x += x_diff
    y += y_diff
    if x < 0 or x >= len(maze[0]) or y < 0 or y >= len(maze) or maze[y][x] == ' ':
        break
    square = maze[y][x]
    steps += 1
    if square == '+':
        if y_diff != 1 and y - 1 >= 0 and (maze[y-1][x] == '|' or maze[y-1][x].isalpha()):
            y_diff = -1
            x_diff = 0
        elif y_diff != -1 and y + 1 < len(maze) and (maze[y+1][x] == '|' or maze[y+1][x].isalpha()):
            y_diff = 1
            x_diff = 0
        elif x_diff != 1 and x - 1 >= 0 and (maze[y][x-1] == '-' or maze[y][x-1].isalpha()):
            y_diff = 0
            x_diff = -1
        elif x_diff != -1 and x + 1 < len(maze[y]) and (maze[y][x+1] == '-' or maze[y][x+1].isalpha()):
            y_diff = 0
            x_diff = 1
    elif square.isalpha():
        seen.append(square)

print "Part One:", ''.join(seen)
print "Part Two:", steps
