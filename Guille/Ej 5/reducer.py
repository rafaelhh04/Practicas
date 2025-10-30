#!/usr/bin/python
# reducer.py para calcular masa promedio por tipo de meteorito
# Calcula el promedio de masa para cada tipo (recclass)

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

    # Si es el mismo tipo, acumular
    if current_type == recclass:
        total_mass += mass
        count += 1
    else:
        # Nuevo tipo: emitir el promedio del tipo anterior
        if current_type:
            average = total_mass / count
            print("{}\t{}".format(current_type, average))

        current_type = recclass
        total_mass = mass
        count = 1

# Emitir el último tipo
if current_type:
    average = total_mass / count
    print("{}\t{}".format(current_type, average))
