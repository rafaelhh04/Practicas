#!/usr/bin/env python3
# reducer.py para calcular masa promedio por tipo de meteorito

import sys

current_type = None
total_mass = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()

    try:
        recclass, mass = line.split('\t', 1)
        mass = float(mass)
    except:
        continue

    if current_type == recclass:
        total_mass += mass
        count += 1
    else:
        if current_type:
            average = total_mass / count
            print("{}\t{:.2f}".format(current_type, average))

        current_type = recclass
        total_mass = mass
        count = 1

if current_type:
    average = total_mass / count
    print("{}\t{:.2f}".format(current_type, average))