#!/usr/bin/python
# reducer.py para calcular precio promedio por anyo
# Calcula el promedio de los precios por anyo

import sys

current_year = None
total_price = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()

    try:
        year, price = line.split('\t', 1)
        price = float(price)
    except:
        continue

    # Si es el mismo anyo, acumular
    if current_year == year:
        total_price += price
        count += 1
    else:
        # Nuevo anyo: emitir el promedio del anyo anterior
        if current_year:
            average = total_price / count
            print("{}\t{}".format(current_year, average))

        current_year = year
        total_price = price
        count = 1

# Emitir el ultimo anyo
if current_year:
    average = total_price / count
    print("{}\t{}".format(current_year, average))
