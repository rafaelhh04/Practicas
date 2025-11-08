#!/usr/bin/env python3
# mapper.py para calcular masa promedio de meteoritos por tipo

import sys
import csv

reader = csv.reader(sys.stdin, delimiter=';') 

# Saltar header
try:
    next(reader)
except StopIteration:
    pass

for line in reader:
    # CSV format: name;id;nametype;recclass;mass (g);fall;year;reclat;reclong;GeoLocation
    if len(line) >= 5:
        try:
            recclass = line[3].strip()
            mass_str = line[4].strip()

            # Ignorar si no tiene masa
            if mass_str and mass_str.lower() not in ['', 'null']:
                mass = float(mass_str)
                print("{}\t{}".format(recclass, mass))
        except:
            continue