#!/usr/bin/python3

import sys


def step(particle_id):
    for dim in range(3):
        particles[particle_id]['v'][dim] += particles[particle_id]['a'][dim]
        particles[particle_id]['p'][dim] += particles[particle_id]['v'][dim]

particles = {}
pid = 0
slowest = (-1, sys.maxint)
while True:
    line = sys.stdin.readline()
    if len(line) > 1:
        particles[pid] = {}
        triples = line.split()
        p = triples[0][3:]
        p = p[0:len(p)-2]
        particles[pid]['p'] = list(map(int, p.split(',')))
        v = triples[1][3:]
        v = v[0:len(v)-2]
        particles[pid]['v'] = list(map(int, v.split(',')))
        a = triples[2][3:]
        a = a[0:len(a)-1]
        particles[pid]['a'] = list(map(int, a.split(',')))
        total_acc = sum(map(lambda a_value: abs(a_value), particles[pid]['a']))
        if total_acc < slowest[1]:
            slowest = (pid, total_acc)
        pid += 1
    else:
        break

print "Part One:", slowest[0]

collision_free_count = 0
collided = False
while True:
    collided = False
    positions = {}
    for pid in particles.keys():
        step(pid)
    for pid, particle in particles.iteritems():
        position = tuple(particle['p'])
        if position in positions:
            positions[position].append(pid)
        else:
            positions[position] = [pid]

    for smashed in positions.values():
        if len(smashed) > 1:
            collision_free_count = 0
            collided = True
            for i in smashed:
                del particles[i]
    if not collided:
        collision_free_count += 1
    if collision_free_count > 100:
        break

print "Part Two:", len(particles)
