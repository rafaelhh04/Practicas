#!/usr/bin/python
# reducer.py para Job 1: Sumar accesos por recurso
# Suma el numero de veces que se accedio a cada recurso

import sys

current_resource = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    resource, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    # Si es el mismo recurso, acumular
    if current_resource == resource:
        current_count += count
    else:
        # Nuevo recurso: emitir el anterior si existe
        if current_resource:
            print("{}\t{}".format(current_resource, current_count))

        current_resource = resource
        current_count = count

# Emitir el ultimo recurso
if current_resource:
    print("{}\t{}".format(current_resource, current_count))
