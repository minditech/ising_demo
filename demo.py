#! /usr/bin/env python
import sys, random, numpy

# Evaluate the energy given a Hamiltonian and configuration
def evaluate_energy(H, cfg):
    tot = 0
    for i in range(len(cfg)-1):
        for j in range(len(cfg)):
            tot += H[i,j]*((-1)**(cfg[i]+cfg[j]))
    return tot

# Read Hamiltonian
N = 300
H = numpy.zeros((N,N))
with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.split()
        spin_a, spin_b, coupling = int(line[0]), int(line[1]), float(line[2])
        H[spin_a,spin_b] = coupling
        H[spin_b,spin_a] = coupling

# Solve Hamiltonian for minimum spin configuration (by random guessing)
min_energy = 1.e9
min_cfg = [0]*N
for i in range(10):
    cfg = [int(2*random.random()) for i in xrange(N)]
    energy = evaluate_energy(H, cfg)
    if energy < min_energy:
        min_energy = energy
        min_cfg = cfg
print min_energy
print 'v '+' '.join(map(str, min_cfg))
